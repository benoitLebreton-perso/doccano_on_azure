from src.find_project_by_name import find_project_by_name
from src.login import login
from src.retro_panai.repositories.data_repository import (
    unzip,
    load_answers,
    load_correction,
)
from src.scoring import scoring
from src.quanters_repository import load_quanters


def main():
    doccano_client = login()
    PROJECT_NAME = "Retro panai"
    retro_panai_project = find_project_by_name(doccano_client, PROJECT_NAME)
    down = doccano_client.download(
        project_id=retro_panai_project.id, format="JSONL", only_approved=False
    )
    print(down.name)
    # TODO unzip and the compute score
    answer_path = unzip(down.name)
    answer_path = "src/retro_panai/data/answers"
    correction = load_correction()
    answers = load_answers(answer_path)
    answers = process_answers(answers, correction)
    leaderboard = compute_leaderboard(answers)
    print("leaderboard\n", leaderboard)
    sorted_image_by_difficulty = sort_question_per_difficulty(answers)
    print("les prez panai qui ont le moins été identifiées\n", sorted_image_by_difficulty)


def process_answers(answers_df, correction_df):
    answers_df = correction_df.merge(
        answers_df, how="left", on="filename"
    ).assign(
        **{
            "score": lambda df: df.apply(
                lambda row: scoring(row["correction"], row["label"]), axis=1
            )
        }
    )
    return answers_df


def compute_leaderboard(processed_answers_df):
    quanters_repo = load_quanters()
    processed_answers_df = (
        processed_answers_df.groupby(by="player")
        .agg({"score": "sum"})
        .sort_values(by="score", ascending=False)
        .reset_index()
        .merge(quanters_repo, left_on="player", right_on="username", how="left")
    )
    return processed_answers_df


def sort_question_per_difficulty(processed_answers_df):
    difficulty_per_image = (
        processed_answers_df.groupby(by="filename")
        .agg({"score": "sum"})
        .sort_values(by="score", ascending=False)
    )
    return difficulty_per_image


if __name__ == "__main__":  # pragma: no cover
    main()
