import os
from doccano_client import DoccanoClient
from src.faceswaps.quanters_repository import load_quanters


URL = os.environ["URL"]
PASSWORD = os.environ["RANDOM_PASSWORD"]
f_d = DoccanoClient(base_url=URL)
f_d.login(username="vgouin", password=PASSWORD)
f_d.get_profile()
users = load_quanters()
users = users["username"]
users = users[0:3]


doccano_clients = [DoccanoClient(base_url=URL) for _ in users]
for user, doccano_client in zip(users, doccano_clients):
    doccano_client.login(username=user, password=PASSWORD)

me_list = [c.get_profile() for c in doccano_clients]
