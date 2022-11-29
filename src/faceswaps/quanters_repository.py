import pandas as pd
import json


def load_quanters():
    quanters_names = pd.read_csv("src/faceswaps/data/quanter_accounts.csv", sep=";")
    # quanters_names = quanters_names.assign(
    #     **{
    #         'username': lambda df: df['Email'].str.extract(pat=r'([^@]+)@quantmetry.com'),
    #         'label': lambda df: df['Prénom'] + " " + df['Nom']
    #         })

    # quanters_names.to_csv("quanter_accounts.csv", sep=";")
    return quanters_names


def create_labels_json():
    quanters_names = load_quanters()
    list_of_quanters = list(quanters_names["label"]) + ["Bruce WILLIS"]
    list_of_quanters = sorted(list_of_quanters)
    list_of_labels = [{"text": label} for label in list_of_quanters]
    with open("labels_quanters.json", "w") as write_file:
        json.dump(list_of_labels, write_file, indent=4)


if __name__ == "__main__":
    create_labels_json()
    quanters = load_quanters()
    from src.login import login

    doccano_client = login()
    PROJECT_ID = 2
    PROJECT_NAME = "QM face swap"
    r_me = doccano_client.get_me()
    list_of_projects = doccano_client.get_project_lsist()["results"]
    project = next(filter(lambda x: x["name"] == PROJECT_NAME, list_of_projects))
    labels = doccano_client.get_category_type_list(project["id"])
