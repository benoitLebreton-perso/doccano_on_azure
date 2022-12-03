import pandas as pd


def load_quanters():
    quanters_names = pd.read_csv("src/faceswaps/data/quanter_accounts.csv", sep=";")
    # quanters_names = quanters_names.assign(
    #     **{
    #         'username': lambda df: df['Email'].str.extract(pat=r'([^@]+)@quantmetry.com'),
    #         'label': lambda df: df['Prénom'] + " " + df['Nom']
    #         })

    # quanters_names.to_csv("quanter_accounts.csv", sep=";")
    return quanters_names
