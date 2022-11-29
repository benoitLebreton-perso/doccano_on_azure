from src.retro_panai.prez_panai_repository import load_prez_repository
from src.retro_panai.labels_repository import load_labels_repository
from src.login import login
from src.upload_images import upload_images
from src.create_labels import create_labels
from src.add_quanters_to_game import add_quanters_to_game


def main():
    doccano_client = login()
    PROJECT_NAME = "Retro panai"
    images_repository = load_prez_repository()
    labels_repository = load_labels_repository()
    project = doccano_client.create_project(
        name=PROJECT_NAME,
        description=PROJECT_NAME,
        project_type="ImageClassification",
        guideline="identifie les prez de panai",
        collaborative_annotation=False,
    )
    uploaded_images_task = upload_images(doccano_client, project, images_repository)
    label_types = create_labels(doccano_client, project, labels_repository)
    members = add_quanters_to_game(doccano_client, project)
    return doccano_client, project, uploaded_images_task, label_types, members


if __name__ == "__main__":
    doccano_client, project, uploaded_images_task, label_types, members = main()
    # doccano_client.user_details.get_current_user_details()
    # doccano_client.get_profile()
    # example_gen = doccano_client.list_examples(project_id=project.id)
    # images_id = [e.id for e in example_gen]
    # doccano_client.list_examples(project_id=5)
    # doccano_client.member.list(project_id=project.id)
    # doccano_client.get_members_progress(project.id)
    # doccano_client.list_roles()
