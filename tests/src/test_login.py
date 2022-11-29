import pytest
from src.login import login
from tests.mock_factory import (
    mock_settings_env_vars,
    mock_doccano_auth,
    mock_profile,
    mock_url,
)


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
