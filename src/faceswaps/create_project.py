from src.add_quanters_to_game import add_quanters_to_game
from src.create_labels import create_labels
from src.faceswaps.face_swap_repository import load_face_swap_repository
from src.faceswaps.quanters_repository import load_quanters
from src.login import login
from src.upload_images import upload_images


def main():
    doccano_client = login()
    quanters = load_quanters()
    face_swaps_repository = load_face_swap_repository()
    project = doccano_client.create_project(
        name="QM face swap",
        description="a QM game",
        project_type="ImageClassification",
        guideline="identifie les quanters derrière ces face swaps",
        collaborative_annotation=False,
    )
    labels = create_labels(doccano_client, project, quanters)
    images = upload_images(doccano_client, project, face_swaps_repository)
    members = add_quanters_to_game(doccano_client, project)
    return (
        doccano_client,
        project,
        quanters,
        face_swaps_repository,
        labels,
        images,
        members,
    )


if __name__ == "__main__":  # pragma: no cover
    (
        doccano_client,
        project,
        quanters,
        face_swaps_repository,
        labels,
        images,
        members,
    ) = main()
    r_me = doccano_client.get_me()
    print(r_me)
