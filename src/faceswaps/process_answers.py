from glob import glob
import re
import os
import pandas as pd

from scoring import scoring
from src.faceswaps.quanters_repository import load_quanters

answer_path = "/Users/blebreton/doccano_on_azure/b6805a9e-f8e5-4b67-9cce-0774a45e2eeb"
glob_path = os.path.join(answer_path, "*")
answers_files = glob(glob_path)

correct_path = os.path.join(answer_path, "admin.jsonl")
correct_answer_pd = pd.read_json(path_or_buf=correct_path, lines=True)
correct_answer_pd = correct_answer_pd.rename(columns={"label": "correction"})



# answer_file = answers_files[3]
# s = re.search(r"([0-9A-Za-z-]+)\.jsonl$", answer_file)
# player = s.groups()[0]
# answer_pd = pd.read_json(path_or_buf=answer_file, lines=True)


answers_of_all_players = []
for answer_file in answers_files:
    s = re.search(r"([0-9A-Za-z-]+)\.jsonl$", answer_file)
    player = s.groups()[0]
    if player == 'admin':
        continue
    answer_pd = pd.read_json(path_or_buf=answer_file, lines=True)
    answer_pd['player'] = player
    answers_of_all_players.append(answer_pd)

answers_of_all_players_pd = pd.concat(answers_of_all_players)
answers_of_all_players_pd = pd.merge(correct_answer_pd, answers_of_all_players_pd, how="left", on="filename")

answers_of_all_players_pd = answers_of_all_players_pd.assign(**{
    'score': lambda df: df.apply(lambda row: scoring(row["correction"], row["label"]), axis=1)
}
)

scores_of_players = answers_of_all_players_pd.groupby(by='player').agg({'score': 'sum'})

scores_of_players = scores_of_players.sort_values(by='score', ascending=False)
# print(scores_of_players)

quanters_repo = load_quanters()
scores_of_players = scores_of_players.reset_index().merge(quanters_repo, left_on='player', right_on='username', how='left')
print(scores_of_players)

difficulty_per_face_swa = answers_of_all_players_pd.groupby(by='filename').agg({'score': 'sum'})
difficulty_per_face_swa = difficulty_per_face_swa.sort_values(by='score', ascending=False)