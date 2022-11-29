import pytest
from src.retro_panai.create_project import main
from doccano_client.models.project import ProjectType
from tests.mock_factory import (
    mock_settings_env_vars,
    mock_profile,
    mock_doccano_auth,
    mock_doccano_create_project,
    mock_doccano_upload,
    mock_doccano_fp_process,
    mock_doccano_task_status,
    mock_doccano_existing_category_types,
    mock_doccano_new_category_types,
    mock_doccano_search_users,
    mock_doccano_search_fakeuser,
    mock_doccano_search_fakeuser2,
    mock_doccano_roles,
    mock_doccano_add_member,
    mock_url,
)


def test_end_to_end_create_project(
    response_mock,
    mock_profile,
    mock_doccano_auth,
    mock_doccano_create_project,
    mock_doccano_upload,
    mock_doccano_fp_process,
    mock_doccano_task_status,
    mock_doccano_existing_category_types,
    mock_doccano_new_category_types,
    mock_doccano_search_users,
    mock_doccano_search_fakeuser,
    mock_doccano_search_fakeuser2,
    mock_doccano_roles,
    mock_doccano_add_member,
):
    project_id = 1
    response_mock_ = response_mock(
        [
            f"POST {mock_url}/v1/auth/login/ -> 200 : {mock_doccano_auth}",
            f"GET {mock_url}/v1/me -> 200 : {mock_profile}",
            f"POST {mock_url}/v1/projects -> 201 : {mock_doccano_create_project}",
            f"POST {mock_url}/v1/fp/process/ -> 201 : {mock_doccano_fp_process}",
            f"GET {mock_url}/v1/tasks/status/1 -> 200 : {mock_doccano_task_status}",
            f"POST {mock_url}/v1/projects/{project_id}/upload -> 201 : {mock_doccano_upload}",
            f"GET {mock_url}/v1/projects/{project_id}/category-types -> 200 : {mock_doccano_existing_category_types}",
            f"POST {mock_url}/v1/projects/{project_id}/category-types -> 200 : {mock_doccano_new_category_types}",
            f"GET {mock_url}/v1/users?q= -> 200 : {mock_doccano_search_users}",
            f"GET {mock_url}/v1/users?q=fakeuser -> 200 : {mock_doccano_search_fakeuser}",
            f"GET {mock_url}/v1/users?q=fakeuser2 -> 200 : {mock_doccano_search_fakeuser2}",
            f"GET {mock_url}/v1/roles -> 200 : {mock_doccano_roles}",
            f"POST {mock_url}/v1/projects/{project_id}/members -> 200 : {mock_doccano_add_member}",
        ]
    )
    with response_mock_:
        doccano_client, project, uploaded_images_task, label_types, members = main()
        user = doccano_client.get_profile()
        assert user.username == "fake_admin"
        assert project.name == "Fake name"
        assert project.project_type == ProjectType.IMAGE_CLASSIFICATION
        assert uploaded_images_task[0].ready
        assert label_types[0].text == "new fake category"
        assert len(members) == 2
        assert members[0].user == 20
