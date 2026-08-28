from InfoApiAuto.asserts.common.response_assert import assert_success_response

EXPECTED_NETWORKS = {
    "All": "all",
    "Solana": "solana",
    "BSC": "bsc",
    "Robinhood": "robinhood",
    "ETH": "eth",
    "BASE": "base"
}

def assert_top_tokens_networks(response):
    response_body = assert_success_response(response)

    data = response_body.get("data")

    assert data is not None, f"热门链类型接口data为null，实际响应：{response_body}"

    actual_networks = data.get("networks")

    assert isinstance(actual_networks, dict), f"热门链类型接口data不是字典类型，实际类型：{type(actual_networks).__name__}"

    for network_name, expected_value in EXPECTED_NETWORKS.items():
        # .get() 的作用就是根据键获取值，actual_value = actual_networks.get("Solana")-->actual_value = "solana"
        actual_value = actual_networks.get(network_name)

        assert actual_value == expected_value, f"{network_name}类型不正确，预期：{expected_value}，实际：{actual_value}"
