import os

from doccano_client import DoccanoClient

from src.quanters_repository import load_quanters
from src.find_project_by_name import find_project_by_name
from src.login import login


URL = os.environ["URL"]
PASSWORD = os.environ["RANDOM_PASSWORD"]
f_d = DoccanoClient(base_url=URL)
f_d.login(username="vgouin", password=PASSWORD)
f_d.get_profile()
users = load_quanters()
users = users["username"]
users = users[0:50]

admin_user = login()

project = find_project_by_name(admin_user, "Retro panai")
label = admin_user.list_label_types(project.id, 'category')[0]
example = next(admin_user.list_examples(project.id))
for i in range(100):
    admin_user.create_category(project_id=project.id, example_id=example.id, label=label.id)
    admin_user.delete_all_categories(project_id=project.id, example_id=example.id)

doccano_clients = [DoccanoClient(base_url=URL) for _ in users]
for user, doccano_client in zip(users, doccano_clients):
    doccano_client.login(username=user, password=PASSWORD)

me_list = [c.get_profile() for c in doccano_clients]
# annotations_list = [c.create_category(project_id=project.id, example_id=example.id, label=label.id) for c in doccano_clients]
# annotations_deletion_list = [c.delete_all_categories(project_id=project.id, example_id=example.id) for c in doccano_clients]

