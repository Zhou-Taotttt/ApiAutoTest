from InfoApiAuto.asserts.common.response_assert import assert_success_response


def assert_collect_radar_success(response, expected_address):
    response_body = assert_success_response(response)

    data = response_body.get("data")

    assert isinstance(data, list), f"data应该是列表，实际类型：{type(data).__name__}"

    actual_address = []
    # 遍历data
    # 使用 data_index 是为了让结构错误时能够指出具体是第几条数据;item 表示一条雷达内容
    for data_index, item in enumerate(data, start=1):
        assert isinstance(item, dict), f"data中第{data_index}条data不是字典，实际类型：{type(item).__name__}"
        entities = item.get("entities")
        assert isinstance(entities, list), (
            f"data中第{data_index}条数据的entities应该是列表，实际类型：{type(entities).__name__}"
        )
        # 遍历entities
        for entity_index, entity  in enumerate(entities, start=1):
            assert isinstance(entity, dict), f"data中第{data_index}条的第{entity_index}条的entity不是字典，实际类型：{type(entity).__name__}"
            contract_address = entity.get("contract_address")
            if contract_address:
                actual_address.append(contract_address)

    assert expected_address in actual_address, f"没有找到收藏地址，无此条情报，预期地址：{expected_address}，实际返回地址：{actual_address}"
    return response_body
