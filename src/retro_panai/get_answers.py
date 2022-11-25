import os
from doccano_client import DoccanoClient


URL = os.environ['URL']
USER = os.environ['ADMIN_USERNAME']
PASSWORD = os.environ['ADMIN_PASSWORD']
doccano_client = DoccanoClient(base_url=URL)
doccano_client.login(username=USER, password=PASSWORD)
PROJECT_NAME = 'Retro panai'


for doccano_project in doccano_client.list_projects():
    if doccano_project.name==PROJECT_NAME:
        retro_panai_project = doccano_project
        break

retro_panai_project
down = doccano_client.download(project_id=retro_panai_project.id, format='JSONL', only_approved=False)
# down # unzip and the compute score