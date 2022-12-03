# Doccano on Azure

## Deployment
Follow the `doccano-deploy.sh` script to deploy your resource.
We need to have an Azure Ressource Group and a running Posgres server in it.
It required the following env variables in your shell (fill the `profile.sh` file from the `profile.sh.template`).

- you choose the admin username, password and email for doccano
  - ADMIN_USERNAME
  - ADMIN_PASSWORD
  - ADMIN_EMAIL
- you find the information about the existing resources
  - SUBSCRIPTION_ID
  - POSTGRES_SERVER_NAME (`az postgres server list --resource-group $RG_NAME | grep fullyQualifiedDomainName`, you also can parse it with `jq`)
  - CREATION_POSTGRES_ADMIN_USERNAME
  - POSTGRES_SERVER_PASSWORD
  - DATABASE_NAME
- when you have deployed your doccano App Service, report the URL in the `profil.sh`

**Activate**
````bash
source profile.sh
````
or 
````
make activate
````

**Launch a new panai retro game**

````bash
make new-panai-retro
````
![Screen-annotation](docs/screen-annotation.png?raw=true "Screen-annotation")


**WIP Get answers**

````bash
make get-retro-panai-answers
````

**Unit testing**

<!-- Pytest Coverage Comment:Begin -->
<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-55%25-orange.svg" /></a><details><summary>Coverage Report </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>src/faceswaps</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/process_answers.py">process_answers.py</a></td><td>30</td><td>30</td><td>0%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/process_answers.py#L1-L71">1&ndash;71</a></td></tr><tr><td colspan="5"><b>src/retro_panai</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/get_answers.py">get_answers.py</a></td><td>30</td><td>30</td><td>0%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/get_answers.py#L1-L63">1&ndash;63</a></td></tr><tr><td colspan="5"><b>src/retro_panai/repositories</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/repositories/data_repository.py">data_repository.py</a></td><td>33</td><td>19</td><td>42%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/repositories/data_repository.py#L20-L21">20&ndash;21</a>, <a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/repositories/data_repository.py#L25-L37">25&ndash;37</a>, <a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/repositories/data_repository.py#L41-L44">41&ndash;44</a></td></tr><tr><td><b>TOTAL</b></td><td><b>174</b></td><td><b>79</b></td><td><b>55%</b></td><td>&nbsp;</td></tr></tbody></table></details>
<!-- Pytest Coverage Comment:End -->

````bash
make tests
````

````bash
make coverage
````

# Scale out

To handle the workload before a massive session :

On Azure portal/App Service resource : Scale-up


![Scale-up](docs/scale-up.png?raw=true "Scale-Up")

To reduce the bill amount between two sessions :

On Azure portal/App Service resource : Scale-up

![Scale-Down](docs/scale-down.png?raw=true "Scale-Down")

## Whitelist the app in the postgres db

Since the postgres database has firewall rules, we need to whitelist our App Service (doccano) resource.
We need to do it again after a scale-up / scale-down because the machines are switched.

Get the outbound addresses of the App Service resource
![Outbound-Addresses](docs/outbound-addresses.png?raw=true "Outbound-Addresses")

And whitlist it in the postgreSQL database.
![Whitelist-IPs](docs/postgres-whitelist.png?raw=true "Whitelist-IPs")

Either manually, or...

### Get the outbound ips of the App Service resource

````bash
export OUTBOUND_IP_ADDRESSES=$(az webapp show --resource-group $RG_NAME --name $WEB_APP_NAME --query outboundIpAddresses --output tsv)
````

### Whitelist all of them in th PostgreSQL resource

````bash
count=0
for i in $(echo $OUTBOUND_IP_ADDRESSES | tr "," "\n")
do
  echo "$i\n"
  az postgres server firewall-rule create --start-ip-address $i --end-ip-address $i --name doccano${count} --resource-group $RG_NAME --server-name qmpostgresql
  let "count+=1" 
  echo "$count\n"
  echo "doccano${count}"
done
````

TODO : if we terraform this infrastructure, this can be simplified.

# Stress test

In order to test if your application is well scaled and will handle the workload.
You can do a stress test. The following test create 100 of simulataneous connections and use the admin account to annotate and un-annotate an image a 100 of times.

````bash
$ python stress_test.py
````

And follow the metric you want (response time for example) on Azure portal App Service resource/Monitoring.

![Monitor-Response-Time](docs/monitor-response-time.png?raw=true "Monitor-Response-Time")