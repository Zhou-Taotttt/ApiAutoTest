import pytest

from InfoApiAuto.asserts.tracking.collected.collected_tokens_assert import assert_collect_tokens_success
from InfoApiAuto.utils.tools import read_json


@pytest.mark.parametrize("case_name,network,address", read_json("collect_tokens.json"))
def test_01_collect_tokens_success(collected_tokens_api, case_name, network, address):
    response = collected_tokens_api.collect_token(network=network, address=address)
    assert_collect_tokens_success(response)