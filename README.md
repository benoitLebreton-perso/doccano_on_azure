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
<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-71%25-yellow.svg" /></a><details><summary>Coverage Report </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>src/faceswaps</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/process_answers.py">process_answers.py</a></td><td>30</td><td>30</td><td>0%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/process_answers.py#L1-L79">1&ndash;79</a></td></tr><tr><td colspan="5"><b>src/retro_panai</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/get_answers.py">get_answers.py</a></td><td>8</td><td>8</td><td>0%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/get_answers.py#L1-L12">1&ndash;12</a></td></tr><tr><td><b>TOTAL</b></td><td><b>129</b></td><td><b>38</b></td><td><b>71%</b></td><td>&nbsp;</td></tr></tbody></table></details>
<!-- Pytest Coverage Comment:End -->

````bash
make tests
````

````bash
make coverage
````