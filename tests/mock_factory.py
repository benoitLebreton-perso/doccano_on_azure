import json
import os
import pytest
from unittest import mock
from doccano_client.models.project import Project
from doccano_client.models.project import ProjectType
from doccano_client.models.task_status import TaskStatus


mock_url = "http://fake@url.com"


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    with mock.patch.dict(
        os.environ,
        {
            "URL": mock_url,
            "ADMIN_USERNAME": "fakeuser",
            "ADMIN_PASSWORD": "fakepassword",
        },
    ):
        yield


@pytest.fixture()
def mock_doccano_auth():
    return json.dumps({"key": "0264a0d944b9a29e6f863a8ce78b076958d766aa"})


@pytest.fixture()
def mock_profile():
    dict_me = {
        "id": 1,
        "username": "fake_admin",
        "is_superuser": True,
        "is_staff": True,
    }
    return json.dumps(dict_me)


@pytest.fixture()
def mock_doccano_create_project():
    project = Project(
        id=1,
        name="Fake name",
        description="Fake description",
        guideline="fake guideline",
        project_type=ProjectType.IMAGE_CLASSIFICATION,
        random_order=False,
        collaborative_annotation=False,
        single_class_classification=False,
        allow_overlapping=False,
        grapheme_mode=False,
    )
    return json.dumps(project.dict())


@pytest.fixture()
def mock_doccano_upload():
    task_status = TaskStatus(ready=True, result={"error": []}, error=None)
    task_id_dict = {"task_id": 1}
    resu_dict = {**task_status.dict(), **task_id_dict}
    return json.dumps(resu_dict)


@pytest.fixture()
def mock_doccano_task_status():
    task_status = TaskStatus(ready=True, result={"error": []}, error=None)
    return json.dumps(task_status.dict())


@pytest.fixture()
def mock_doccano_existing_category_types():
    from doccano_client.models.label_type import CategoryType

    a_category_type = CategoryType(
        id=1, text="fake category", background_color="#3d3bc6", text_color="#ffffff"
    )
    return json.dumps([a_category_type.dict()])


@pytest.fixture()
def mock_doccano_new_category_types():
    from doccano_client.models.label_type import CategoryType

    a_category_type = CategoryType(id=2, text="new fake category")
    return json.dumps(a_category_type.dict())


@pytest.fixture()
def mock_doccano_fp_process():
    return json.dumps("")


@pytest.fixture()
def mock_doccano_search_users():
    from doccano_client.models.user import User

    a_fake_user = User(id=20, username="fakeuser", is_superuser=False, is_staff=False)
    another_fake_user = User(
        id=21, username="fakeuser2", is_superuser=False, is_staff=False
    )
    return json.dumps([a_fake_user.dict(), another_fake_user.dict()])


@pytest.fixture()
def mock_doccano_search_fakeuser():
    from doccano_client.models.user import User

    a_fake_user = User(id=20, username="fakeuser", is_superuser=False, is_staff=False)
    return json.dumps([a_fake_user.dict()])


@pytest.fixture()
def mock_doccano_search_fakeuser2():
    from doccano_client.models.user import User

    another_fake_user = User(
        id=21, username="fakeuser2", is_superuser=False, is_staff=False
    )
    return json.dumps([another_fake_user.dict()])


@pytest.fixture()
def mock_doccano_roles():
    from doccano_client.models.role import Role

    admin = Role(id=1, name="project_admin")
    annotator = Role(id=2, name="annotator")
    annotation_approver = Role(id=3, name="annotation_approver")
    return json.dumps([admin.dict(), annotator.dict(), annotation_approver.dict()])


@pytest.fixture()
def mock_doccano_add_member():
    from doccano_client.models.member import Member

    new_member = Member(user=20, role=3)
    return json.dumps(new_member.dict())
