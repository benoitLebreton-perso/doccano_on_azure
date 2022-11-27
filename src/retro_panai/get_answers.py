from src.login import login


def main():
    doccano_client = login()
    PROJECT_NAME = 'Retro panai'


    for doccano_project in doccano_client.list_projects():
        if doccano_project.name==PROJECT_NAME:
            retro_panai_project = doccano_project
            break

    retro_panai_project
    down = doccano_client.download(project_id=retro_panai_project.id, format='JSONL', only_approved=False)
    # down 
    # # unzip and the compute score

if __name__ == '__main__':
    main()