from InfoApiAuto.asserts.tracking.hot.networks_assert import  assert_top_tokens_networks

def test_01_top_tokens_networks_success(hot_api):
    response = hot_api.get_top_tokens_networks()
    assert_top_tokens_networks(response)

