import pandas as pd


def load_labels_repository():
    prez_panai = pd.read_csv('src/retro_panai/data/prez_panai_repository.csv')
    return prez_panai