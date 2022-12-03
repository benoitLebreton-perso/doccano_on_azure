# Doccano on Azure
**Activate**
````bash
source profile.sh
````
or 
````
make activate
````


**Stress test**

To check that the application is well scaled use the python script : stress_test.py


**Launch a new panai retro game**
````bash
make new-panai-retro
````

**WIP Get answers**
````bash
make get-retro-panai-answers
````

**Unit testing**

<!-- Pytest Coverage Comment:Begin -->
<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-71%25-yellow.svg" /></a><details><summary>Coverage Report </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>src/faceswaps</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/process_answers.py">process_answers.py</a></td><td>30</td><td>30</td><td>0%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/process_answers.py#L1-L71">1&ndash;71</a></td></tr><tr><td colspan="5"><b>src/retro_panai</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/get_answers.py">get_answers.py</a></td><td>8</td><td>8</td><td>0%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/get_answers.py#L1-L12">1&ndash;12</a></td></tr><tr><td><b>TOTAL</b></td><td><b>129</b></td><td><b>38</b></td><td><b>71%</b></td><td>&nbsp;</td></tr></tbody></table></details>
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
...
````

TODO : if we terraform this infrastructure, this can be simplified.
