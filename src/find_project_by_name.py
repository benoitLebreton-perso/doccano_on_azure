def find_project_by_name(doccano_client, name):
    for doccano_project in doccano_client.list_projects():
        if doccano_project.name == name:
            found_project = doccano_project
            break
    if not found_project:
        raise KeyError("The {name} doccano project does not exist")
    return found_project