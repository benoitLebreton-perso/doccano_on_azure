import pytest

from src.find_project_by_name import find_project_by_name
from src.login import login
from tests.conftest import mock_url


@pytest.mark.unit
def test_find_project_by_name(
    response_mock, mock_doccano_auth, mock_doccano_get_projects
):
    response_mock_ = response_mock(
        [
            f"POST {mock_url}/v1/auth/login/ -> 200 : {mock_doccano_auth}",
            f"GET {mock_url}/v1/projects -> 200 : {mock_doccano_get_projects}",
        ]
    )
    with response_mock_:
        doccano_client = login()
        name = "Fake name"
        found_project = find_project_by_name(doccano_client, name)
        assert found_project.name == name


@pytest.mark.unit
def test_raise_project_not_found(
    response_mock, mock_doccano_auth, mock_doccano_get_projects
):
    response_mock_ = response_mock(
        [
            f"POST {mock_url}/v1/auth/login/ -> 200 : {mock_doccano_auth}",
            f"GET {mock_url}/v1/projects -> 200 : {mock_doccano_get_projects}",
        ]
    )
    with (pytest.raises(ValueError) as exc_info, response_mock_):
        doccano_client = login()
        name = "Fake name that does not exist"
        find_project_by_name(doccano_client, name)
        assert exc_info.value.args[0] == f"The {name} doccano project does not exist"
