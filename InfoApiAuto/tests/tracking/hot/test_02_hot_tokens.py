from InfoApiAuto.asserts.tracking.hot.tokens_assert import assert_top_tokens

def test_01_top_tokens_solana_success(hot_api):
    response = hot_api.get_top_tokens(network="solana")
    assert_top_tokens(response, expect_network="solana")

def test_02_top_tokens_bsc_success(hot_api):
    response = hot_api.get_top_tokens(network="bsc")
    assert_top_tokens(response, expect_network="bsc")

def test_03_top_tokens_eth_success(hot_api):
    response = hot_api.get_top_tokens(network="eth")
    assert_top_tokens(response, expect_network="eth")

def test_04_top_tokens_base_success(hot_api):
    response = hot_api.get_top_tokens(network="base")
    assert_top_tokens(response, expect_network="base")

def test_05_top_tokens_robinhood_success(hot_api):
    response = hot_api.get_top_tokens(network="robinhood")
    assert_top_tokens(response, expect_network="robinhood")