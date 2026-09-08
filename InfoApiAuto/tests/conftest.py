import pytest

from InfoApiAuto.api.auth.login_api import LoginApi
from InfoApiAuto.api.tracking.collect_radar_api import CollectRadarApi
from InfoApiAuto.api.tracking.collected_tokens_api import CollectedTokensApi
from InfoApiAuto.api.tracking.hot_api import HotApi
from InfoApiAuto.asserts.auth.login_assert import assert_login_success
from InfoApiAuto.config.settings import Settings
from InfoApiAuto.core.http_client import HttpClient

@pytest.fixture(scope="session")
def authenticated_client():
    Settings.validate()
    client = HttpClient(base_url=Settings.BASE_URL, timeout=Settings.REQUEST_TIMEOUT)
    # 创建登录接口对象
    login_api = LoginApi(client)
    # 调用登录接口
    response = login_api.login(email=Settings.TEST_EMAIL, code=Settings.TEST_CODE)
    # 调用登录断言
    access_token = assert_login_success(response)
    # 设置token
    client.set_access_token(access_token)
    # 返回已认证客户端
    yield client

    client.close()


@pytest.fixture(scope="session")
def hot_api(authenticated_client):
    return HotApi(authenticated_client)

@pytest.fixture(scope="session")
def collected_tokens_api(authenticated_client):
    return CollectedTokensApi(authenticated_client)

@pytest.fixture(scope="session")
def collect_radar_api(authenticated_client):
    return CollectRadarApi(authenticated_client)