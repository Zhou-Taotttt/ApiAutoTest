import pytest

from InfoApiAuto.asserts.tracking.collected.collect_radar_assert import assert_collect_radar_success
from InfoApiAuto.asserts.tracking.collected.collected_tokens_assert import assert_collect_tokens_success
from InfoApiAuto.utils.tools import read_json


@pytest.mark.parametrize("case_name,network,address", read_json("collect_tokens.json"))
def test_03_collect_radar(collected_tokens_api, collect_radar_api, case_name, network, address):
    collect_response = collected_tokens_api.collect_token(network=network, address=address)
    assert_collect_tokens_success(collect_response)

    radar_response = collect_radar_api.get_collect_radar()
    assert_collect_radar_success(radar_response, expected_address=address)
