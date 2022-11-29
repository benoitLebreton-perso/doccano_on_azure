from src.login import login
from src.find_project_by_name import find_project_by_name


def main():
    doccano_client = login()
    PROJECT_NAME = "Retro panai"
    retro_panai_project = find_project_by_name(doccano_client, PROJECT_NAME)
    down = doccano_client.download(
        project_id=retro_panai_project.id, format="JSONL", only_approved=False
    )
    print(down.name)
    # TODO unzip and the compute score


if __name__ == "__main__":
    main()
