import json
from pathlib import Path
# 定位数据根目录,parents[0] = InfoApiAuto/utils，parents[1] = InfoApiAuto
DATA_DIR = Path(__file__).resolve().parents[1]/"data"

def read_json(file_name):
    data = []
    # 递归查找文件
    match_files = list(DATA_DIR.rglob(file_name))
    if not match_files:
        raise FileNotFoundError(f"在{DATA_DIR}中未找到JSON文件：{file_name}")

    if len(match_files) > 1:
        raise ValueError(f"存在多个同名JSON文件：{file_name}")

    files_path = match_files[0]
    # 打开解析JSON
    with files_path.open(mode="r", encoding="utf-8") as file:
        # JSON 内容会转换为 Python 列表，保存到 temp
        temp = json.load(file)
    #将每组字典转换成元组
    for item in temp:
        case = tuple(item.values())
        data.append(case)

    return data