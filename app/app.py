from collections import defaultdict
from typing import List

def dedupe_header(columns: List[str]) -> List[str]:
    """
    通过附加数字后缀使重复的列名唯一化
    
    规则：
    - 第一个出现的名称保持原样
    - 第二个、第三个...重复名称添加 ".1", ".2" 等后缀
    - 保持原始顺序不变
    - 输入是字符串列表（列名），输出是相同长度的列表
    
    示例：
    ["id", "name", "id", "name", "name"] -> ["id", "name", "id.1", "name.1", "name.2"]
    """
    seen_counts = defaultdict(int)
    result: List[str] = []

    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[col] += 1

    return result