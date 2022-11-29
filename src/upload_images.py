from doccano_client.models.data_upload import Task


def upload_images(doccano_client, project, images_repository):
    tasks = []
    for _, prez in images_repository.iterrows():
        prez_filepath = prez["filepath"]
        image_task = doccano_client.upload(
            project_id=project.id,
            file_paths=[prez_filepath],
            task=Task.IMAGE_CLASSIFICATION,
            format="ImageFile",
        )
        tasks.append(image_task)
    return tasks
