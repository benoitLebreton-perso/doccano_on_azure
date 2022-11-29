import pandas as pd


def load_face_swap_repository():
    prez_panai = pd.read_csv("src/faceswaps/data/face_swaps_repository.csv")
    return prez_panai
