import os
from doccano_client import DoccanoClient


def login():
    URL = os.environ["URL"]
    USER = os.environ["ADMIN_USERNAME"]
    PASSWORD = os.environ["ADMIN_PASSWORD"]
    doccano_client = DoccanoClient(base_url=URL)
    doccano_client.login(username=USER, password=PASSWORD)
    return doccano_client
