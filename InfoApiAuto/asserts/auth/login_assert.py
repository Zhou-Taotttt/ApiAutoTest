from InfoApiAuto.asserts.common.response_assert import assert_success_response


def assert_login_success(response):
    response_body = assert_success_response(response)

    data = response_body.get("data")
    assert data is not None, (
        f"登录响应中data为null，实际响应：{response_body}"
    )

    assert isinstance(data, dict), (
        f"登录响应中data不是字典类型，实际类型：{type(data).__name__}"
    )

    access_token = data.get("access_token")

    assert access_token, (
        f"登录响应中缺少access_token，实际响应：{response_body}"
    )

    return access_token