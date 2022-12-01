def find_project_by_name(doccano_client, name):
    list_of_projects = doccano_client.list_projects()
    try:
        found_project = next(filter(lambda x: x.name == name, list_of_projects))
    except StopIteration:
        raise ValueError(f"The {name} doccano project does not exist")
    return found_project
