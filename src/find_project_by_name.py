def find_project_by_name(doccano_client, name):
    list_of_projects = doccano_client.list_projects()
    found_project= next(filter(lambda x: x["name"] == name, list_of_projects))
    if not found_project:
        raise KeyError("The {name} doccano project does not exist")
    return found_project