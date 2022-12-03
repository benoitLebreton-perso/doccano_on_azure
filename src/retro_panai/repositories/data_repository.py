import re
import os
import pandas as pd
import zipfile

from glob import glob


def load_labels_repository():
    prez_panai = pd.read_csv("src/retro_panai/data/labels_repository.csv")
    return prez_panai


def load_prez_repository():
    prez_panai = pd.read_csv("src/retro_panai/data/prez_panai_repository.csv")
    return prez_panai


def unzip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("src/retro_panai/data/answers")


def load_answers(answer_path):
    glob_path = f"{answer_path}/*"
    answers_files = glob(glob_path)
    answers_of_all_players = []
    for answer_file in answers_files:
        s = re.search(r"([0-9A-Za-z-]+)\.jsonl$", answer_file)
        player = s.groups()[0]
        if player == "admin":
            continue
        answer_pd = pd.read_json(path_or_buf=answer_file, lines=True)
        answer_pd["player"] = player
        answers_of_all_players.append(answer_pd)
        answers_all_players = pd.concat(answers_of_all_players)
    return answers_all_players


def load_correction(answer_path):
    correct_path = os.path.join(answer_path, "admin.jsonl")
    correct_answer_pd = pd.read_json(path_or_buf=correct_path, lines=True)
    correct_answer_pd = correct_answer_pd.rename(columns={"label": "correction"})
    return correct_answer_pd
