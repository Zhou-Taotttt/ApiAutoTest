from InfoApiAuto.asserts.common.response_assert import assert_success_response

def assert_top_tokens(response, expect_network):
    response_body = assert_success_response(response)

    data = response_body.get("data")
    assert data is not None, f"{expect_network}热门代币接口中data为null，实际响应：{response_body}"
    assert isinstance(data, dict), f"{expect_network}热门代币接口中data不是字典类型，实际类型为：{type(data).__name__}"

    tokens = data.get("tokens")
    assert isinstance(tokens, list), f"{expect_network}热门代币接口中tokens不是列表类型，实际类型为：{type(tokens).__name__}"
    assert tokens, f"{expect_network}热门代币接口没有返回代币数据"

    for token in tokens:
        assert isinstance(token, dict), f"{expect_network}热门代币接口的代币数据不是字典类型"

        actual_network = token.get("network")
        assert actual_network, f"{expect_network}热门代币接口的代币缺少network字段"

        assert str(actual_network).lower() == str(expect_network).lower(), (
            f"{expect_network}热门代币接口中存在链类型错误的代币，代币：{token.get('symbol')}，预期链：{expect_network}，实际链：{actual_network}"
        )


