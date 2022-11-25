import os
from doccano_client import DoccanoClient
from doccano_client.models.data_upload import Task
from src.retro_panai.prez_panai_repository import load_prez_panai


URL = os.environ['URL']
USER = os.environ['ADMIN_USERNAME']
PASSWORD = os.environ['ADMIN_PASSWORD']
doccano_client = DoccanoClient(base_url=URL)
doccano_client.login(username=USER, password=PASSWORD)
PROJECT_NAME = 'Retro panai'

doccano_client.user_details.get_current_user_details()
doccano_client.get_profile()

project = doccano_client.create_project(
    name=PROJECT_NAME,
    description=PROJECT_NAME,
    project_type="ImageClassification",
    guideline="identifie les prez de panai",
    collaborative_annotation=False
)

prez_panai = load_prez_panai()
for _, prez in prez_panai.iterrows():
    prez_filepath = prez["filepath"]
    image = doccano_client.upload(
        project_id=project.id, 
        file_paths=[prez_filepath], 
        task=Task.IMAGE_CLASSIFICATION,
        format="ImageFile")

# example_gen = doccano_client.list_examples(project_id=project.id)
# images_id = [e.id for e in example_gen]



for _, prez in prez_panai.iterrows():
    prez_name = prez["name"]
    print(prez_name)
    doccano_client.create_label_type(
        project_id=project.id,
        type="category",
        text=prez_name,
        )
    
doccano_client.get_examples(project_id=5)

down = doccano_client.download(project_id=project.id, format='JSONL', only_approved=False)
down # unzip and the compute score


doccano_client.member.list(5)

doccano_client.add_member(project_id=project.id, username="cvandevelde", role_name="project_admin")

doccano_client.get_members_progress(5)

users = doccano_client.search_users()

for user in users:
    doccano_client.add_member(project_id=project.id, username=user.username, role_name="project_admin")

doccano_client.list_roles()
