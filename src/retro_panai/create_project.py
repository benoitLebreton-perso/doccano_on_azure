from src.add_quanters_to_game import add_quanters_to_game
from src.create_labels import create_labels
from src.login import login
from src.retro_panai.repositories.data_repository import (
    load_labels_repository,
    load_prez_repository,
)
from src.upload_images import upload_images


def main():
    doccano_client = login()
    labels_repository = load_labels_repository()
    images_repository = load_prez_repository()
    project = doccano_client.create_project(
        name="Retro panai",
        description="Retro panai",
        project_type="ImageClassification",
        guideline="identifie les prez de panai",
        collaborative_annotation=False,
    )
    label_types = create_labels(doccano_client, project, labels_repository)
    uploaded_images_task = upload_images(doccano_client, project, images_repository)
    members = add_quanters_to_game(doccano_client, project)
    return (
        doccano_client,
        project,
        images_repository,
        label_types,
        uploaded_images_task,
        members,
    )


if __name__ == "__main__":  # pragma: no cover
    (
        doccano_client,
        project,
        images_repository,
        label_types,
        uploaded_images_task,
        members,
    ) = main()
    doccano_client.user_details.get_current_user_details()
    doccano_client.get_profile()
    example_gen = doccano_client.list_examples(project_id=project.id)
    images_id = [e.id for e in example_gen]
    doccano_client.list_examples(project_id=project.id)
    doccano_client.member.list(project_id=project.id)
    doccano_client.get_members_progress(project.id)
    doccano_client.list_roles()
