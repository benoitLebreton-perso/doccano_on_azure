# ----------------
# Require :
# ADMIN_USERNAME
# ADMIN_PASSWORD
# ADMIN_EMAIL
# SUBSCRIPTION_ID
# POSTGRES_SERVER_NAME
# CREATION_POSTGRES_ADMIN_USERNAME
# POSTGRES_SERVER_PASSWORD
# DATABASE_NAME
# ----------------

# Resource group parameters
RG_NAME=QM_MLFlow
RG_LOCATION=westeurope

# Container registry parameters
ACR_NAME=mlflowacr

# Docker image parameters
DOCKER_IMAGE_NAME=doccano
DOCKER_IMAGE_TAG=latest

# App service plan parameters
ASP_NAME=doccano-service-plan

# Web app parameters
WEB_APP_NAME=qmdoccano

# Label studio settings
STUDIO_HOST=0.0.0.0
STUDIO_PORT=8000
STUDIO_WORKERS=1

STORAGE_ACCOUNT_NAME=qmdoccano
STORAGE_CONTAINER_NAME=content

# az postgres server show --resource-group $RG_NAME --name qmpostgresql

echo "Logging into Azure"
az login

echo "Setting default subscription: $SUBSCRIPTION_ID"
az account set \
--subscription $SUBSCRIPTION_ID

echo "Creating storage account: $STORAGE_ACCOUNT_NAME"
az storage account create \
 --resource-group $RG_NAME \
 --location $RG_LOCATION \
 --name $STORAGE_ACCOUNT_NAME \
 --sku Standard_LRS

echo "Creating storage container: $STORAGE_CONTAINER_NAME"
az storage container create \
 --name $STORAGE_CONTAINER_NAME \
 --account-name $STORAGE_ACCOUNT_NAME

echo "Exporting storage keys: $STORAGE_ACCOUNT_NAME"
export STORAGE_ACCESS_KEY=$(az storage account keys list --resource-group $RG_NAME --account-name $STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv)
export STORAGE_CONNECTION_STRING=`az storage account show-connection-string --resource-group $RG_NAME --name $STORAGE_ACCOUNT_NAME --output tsv`


echo "Getting Azure container registry credentials: $ACR_NAME"
export ACR_USERNAME=$(az acr credential show --name $ACR_NAME --query "username" --output tsv)
export ACR_PASSWORD=$(az acr credential show --name $ACR_NAME --query "passwords[0].value" --output tsv)

export ARTIFACTS_ROOT="wasbs://${STORAGE_CONTAINER_NAME}@${STORAGE_ACCOUNT_NAME}.blob.core.windows.net/artifacts"

echo "Logging into Azure container registry"
sudo docker login $ACR_NAME.azurecr.io \
--username "$ACR_USERNAME" \
--password "$ACR_PASSWORD"

# echo "Building Docker image from file: $DOCKER_IMAGE_NAME"
# sudo docker build \
# --tag $DOCKER_IMAGE_NAME \
# --file Dockerfile . \
# --no-cache
# cd ..

STUDIO_FILESTORE="postgresql://${CREATION_POSTGRES_ADMIN_USERNAME}:${POSTGRES_SERVER_PASSWORD}@${POSTGRES_SERVER_NAME}:5432/${DATABASE_NAME}"
echo $STUDIO_FILESTORE

# --env STUDIO_SERVER_DEFAULT_ARTIFACT_ROOT=$ARTIFACTS_ROOT \
# --env AZURE_STORAGE_CONNECTION_STRING=$STORAGE_CONNECTION_STRING \

# local test
sudo docker run -p 8000:8000 \
--env ADMIN_USERNAME=$ADMIN_USERNAME \
--env ADMIN_PASSWORD=$ADMIN_PASSWORD \
--env ADMIN_EMAIL=$ADMIN_EMAIL \
--env DATABASE_URL=$STUDIO_FILESTORE \
-it doccano/doccano:latest

# ATTENTION il faut créer la database "labelstudio" dans postgres. 
# Mais il faut ajouter l'IP de l'ordinateur et des VM et de tous les ordi qui auront besoin de ça sur l'azure database ! 
# Sinon on a l'erreur : psql: error: FATAL:  no pg_hba.conf entry for host "80.236.40.170", user "qmpostgresql", database "qmpostgres@qmpostgresql", SSL on
# Ou sinon on désactive SSL ?
# depuis une connexion dbeaver j'ai créé une database sur la tablespace "Default" (et non "pg_default") et le user "qmpostgres"



# echo "Pushing image to Azure container registry: $ACR_NAME"
# sudo docker tag $DOCKER_IMAGE_NAME $ACR_NAME.azurecr.io/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG
docker tag doccano/doccano $ACR_NAME.azurecr.io/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG
sudo docker push $ACR_NAME.azurecr.io/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG

# echo "Showing pushed images"
# az acr repository list \
# --name $ACR_NAME

echo "Creating app service plan: $ASP_NAME"
az appservice plan create \
--name $ASP_NAME \
--resource-group $RG_NAME \
--sku S1 \
--is-linux

echo "Creating web app: $WEB_APP_NAME"
az webapp create \
--resource-group $RG_NAME \
--plan $ASP_NAME \
--name $WEB_APP_NAME \
--deployment-container-image-name $ACR_NAME.azurecr.io/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG

echo "Configuring registry credentials in web app"
az webapp config container set \
--name $WEB_APP_NAME \
--resource-group $RG_NAME \
--docker-custom-image-name $ACR_NAME.azurecr.io/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG \
--docker-registry-server-url https://$ACR_NAME.azurecr.io \
--docker-registry-server-user $ACR_USERNAME \
--docker-registry-server-password $ACR_PASSWORD \
--enable-app-service-storage true


echo "Setting Azure container registry credentials"
az webapp config appsettings set \
--resource-group $RG_NAME \
--name $WEB_APP_NAME \
--settings WEBSITES_PORT=$STUDIO_PORT

echo "Enabling access to logs generated from inside the container"
az webapp log config \
--name $WEB_APP_NAME \
--resource-group $RG_NAME \
--docker-container-logging filesystem

echo "Setting environment variables"
# az webapp config appsettings set \
# --resource-group $RG_NAME \
# --name $WEB_APP_NAME \
# --settings AZURE_STORAGE_CONNECTION_STRING=$STORAGE_CONNECTION_STRING
# az webapp config appsettings set \
# --resource-group $RG_NAME \
# --name $WEB_APP_NAME \
# --settings STUDIO_SERVER_DEFAULT_ARTIFACT_ROOT=$ARTIFACTS_ROOT
az webapp config appsettings set \
--resource-group $RG_NAME \
--name $WEB_APP_NAME \
--settings STUDIO_SERVER_WORKERS=$STUDIO_WORKERS
az webapp config appsettings set \
--resource-group $RG_NAME \
--name $WEB_APP_NAME \
--settings STUDIO_SERVER_PORT=$STUDIO_PORT
az webapp config appsettings set \
--resource-group $RG_NAME \
--name $WEB_APP_NAME \
--settings STUDIO_SERVER_HOST=$STUDIO_HOST
az webapp config appsettings set \
--resource-group $RG_NAME \
--name $WEB_APP_NAME \
--settings DATABASE_URL=$STUDIO_FILESTORE

az webapp config appsettings set \
--resource-group $RG_NAME \
--name $WEB_APP_NAME \
--settings ADMIN_USERNAME=$ADMIN_USERNAME

az webapp config appsettings set \
--resource-group $RG_NAME \
--name $WEB_APP_NAME \
--settings ADMIN_EMAIL=$ADMIN_EMAIL

az webapp config appsettings set \
--resource-group $RG_NAME \
--name $WEB_APP_NAME \
--settings ADMIN_PASSWORD=$ADMIN_PASSWORD

az webapp config appsettings set \
--resource-group $RG_NAME \
--name $WEB_APP_NAME \
--settings PGSSLMODE='require'

az webapp config appsettings set \
--resource-group $RG_NAME \
--name $WEB_APP_NAME \
--settings AZURE_BLOB_ACCOUNT_NAME=$STORAGE_ACCOUNT_NAME

az webapp config appsettings set \
--resource-group $RG_NAME \
--name $WEB_APP_NAME \
--settings AZURE_BLOB_ACCOUNT_KEY=$STORAGE_ACCESS_KEY


# add ip to postgresql instance firewall
az webapp show --resource-group $RG_NAME --name $WEB_APP_NAME --query outboundIpAddresses --output tsv

# manually add the IP addresses to the postgres


echo "Linking storage account to web app"
az webapp config storage-account add \
 --resource-group $RG_NAME \
 --name $WEB_APP_NAME \
 --custom-id $STORAGE_ACCOUNT_NAME \
 --storage-type AzureBlob \
 --share-name $STORAGE_CONTAINER_NAME \
 --account-name $STORAGE_ACCOUNT_NAME \
 --access-key $STORAGE_ACCESS_KEY
 --mount-path $STORAGE_MOUNT_POINT

echo "Verify linked storage account: $STORAGE_ACCOUNT_NAME"
az webapp config storage-account list \
 --resource-group $RG_NAME \
 --name $WEB_APP_NAME