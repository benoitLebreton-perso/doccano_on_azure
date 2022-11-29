def add_quanters_to_game(doccano_client, project):
    users = doccano_client.search_users()
    members = [
        doccano_client.add_member(project.id, user.username, "annotator")
        for user in users
        if user.username != "admin"
    ]
    return members
