import pandas as pd


def load_prez_panai():
    prez_panai = pd.read_csv('src/retro_panai/prez_panai.csv')
    return prez_panai

if __name__ == '__main__':
    prez_panai = load_prez_panai()