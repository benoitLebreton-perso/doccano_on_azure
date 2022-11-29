import pytest
from src.login import login
from tests.conftest import mock_url


@pytest.mark.unit
def test_login(response_mock, mock_doccano_auth, mock_profile):
    response_mock_ = response_mock(
        [
            f"POST {mock_url}/v1/auth/login/ -> 200 : {mock_doccano_auth}",
            f"GET {mock_url}/v1/me -> 200 : {mock_profile}",
        ]
    )
    with response_mock_:
        doccano_client = login()
        user = doccano_client.get_profile()
        assert user.username == "fake_admin"
