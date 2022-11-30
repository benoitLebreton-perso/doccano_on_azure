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
<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/README.md"><img alt="Coverage" src="https://img.shields.io/badge/Coverage-57%25-orange.svg" /></a><details><summary>Coverage Report </summary><table><tr><th>File</th><th>Stmts</th><th>Miss</th><th>Cover</th><th>Missing</th></tr><tbody><tr><td colspan="5"><b>src</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/find_project_by_name.py">find_project_by_name.py</a></td><td>6</td><td>6</td><td>0%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/find_project_by_name.py#L1-L6">1&ndash;6</a></td></tr><tr><td colspan="5"><b>src/faceswaps</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/create_project.py">create_project.py</a></td><td>19</td><td>3</td><td>84%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/create_project.py#L35-L45">35&ndash;45</a></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/process_answers.py">process_answers.py</a></td><td>30</td><td>30</td><td>0%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/process_answers.py#L1-L79">1&ndash;79</a></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/quanters_repository.py">quanters_repository.py</a></td><td>23</td><td>16</td><td>30%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/quanters_repository.py#L18-L23">18&ndash;23</a>, <a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/faceswaps/quanters_repository.py#L27-L37">27&ndash;37</a></td></tr><tr><td colspan="5"><b>src/retro_panai</b></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/create_project.py">create_project.py</a></td><td>17</td><td>1</td><td>94%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/create_project.py#L35">35</a></td></tr><tr><td>&nbsp; &nbsp;<a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/get_answers.py">get_answers.py</a></td><td>10</td><td>10</td><td>0%</td><td><a href="https://github.com/benoitLebreton-perso/doccano_on_azure/blob/main/src/retro_panai/get_answers.py#L1-L17">1&ndash;17</a></td></tr><tr><td><b>TOTAL</b></td><td><b>154</b></td><td><b>66</b></td><td><b>57%</b></td><td>&nbsp;</td></tr></tbody></table></details>
<!-- Pytest Coverage Comment:End -->

````bash
make tests
````

````bash
make coverage
````