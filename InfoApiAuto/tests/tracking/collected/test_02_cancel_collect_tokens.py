import pytest

from InfoApiAuto.asserts.tracking.collected.collected_tokens_assert import assert_collect_tokens_success, assert_cancel_tokens_success
from InfoApiAuto.utils.tools import read_json


@pytest.mark.parametrize("case_name,network,address", read_json("cancel_collect_tokens.json"))
def test_01_cancel_collect_tokens_success(collected_tokens_api, case_name, network, address):
    # 清理已存在的收藏状态
    collected_tokens_api.cancel_collect_token(network=network, address=address)

    # 建立取消收藏所需的已收藏状态
    collect_response = collected_tokens_api.collect_token(network=network, address=address)
    assert_collect_tokens_success(collect_response)

    cancel_response = collected_tokens_api.cancel_collect_token(network=network, address=address)
    assert_cancel_tokens_success(cancel_response)
