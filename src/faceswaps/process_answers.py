import os
import re
from glob import glob

import pandas as pd

from quanters_repository import load_quanters
from src.scoring import scoring

quanters_repo = load_quanters()
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
    if player == "admin":
        continue
    answer_pd = pd.read_json(path_or_buf=answer_file, lines=True)
    answer_pd["player"] = player
    answers_of_all_players.append(answer_pd)
    answers_all_players = pd.concat(answers_of_all_players)

answers_all_players = correct_answer_pd.merge(
    answers_all_players, how="left", on="filename"
).assign(
    **{
        "score": lambda df: df.apply(
            lambda row: scoring(row["correction"], row["label"]), axis=1
        )
    }
)

scores_of_players = (
    answers_all_players.groupby(by="player")
    .agg({"score": "sum"})
    .sort_values(by="score", ascending=False)
    .reset_index()
    .merge(quanters_repo, left_on="player", right_on="username", how="left")
)

print("leaderboard")
print(scores_of_players)

# difficulty_per_face_swa = (
#     answers_of_all_players_pd.groupby(by="filename")
#     .agg({"score": "sum"})
#     .sort_values(by="score", ascending=False)
# )

difficulty_per_face_swa = (
    answers_all_players.groupby(by="filename")
    .agg({"score": "sum"})
    .sort_values(by="score", ascending=False)
)

print("most difficult swap")
print(difficulty_per_face_swa)
