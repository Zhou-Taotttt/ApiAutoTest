import pytest

# 处理 HTTP 状态码、解析JSON 格式
def parse_json_response(response):
    assert response.status_code == 200, (
        f"HTTP请求失败，状态码：{response.status_code}，响应内容：{response.text}"
    )

    try:
        response_body = response.json()
    except ValueError:
        pytest.fail(
            f"接口没有返回合法JSON，响应内容：{response.text}"
        )
    assert isinstance(response_body, dict), (
        f"接口JSON响应应该是字典，实际类型：{type(response_body).__name__}"
    )

    return response_body

def assert_success_response(response):
    response_body = parse_json_response(response)

    actual_code = response_body.get("code")

    assert actual_code == 0, f"接口业务请求失败，预期code:0，实际code：{actual_code}"

    actual_msg =response_body.get("msg")

    assert actual_msg == "success", f"接口业务消息不正确，预期msg:success，实际msg:{actual_msg}"

    return response_body