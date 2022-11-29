def create_labels(doccano_client, project, labels_repository):
    label_types = []
    for _, prez in labels_repository.iterrows():
        prez_name = prez["label"]
        label_type = doccano_client.create_label_type(
            project_id=project.id,
            type="category",
            text=prez_name,
        )
        label_types.append(label_type)
    return label_types
