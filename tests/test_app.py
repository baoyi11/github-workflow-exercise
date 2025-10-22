from app.app import dedupe_header
from app.app import add_numbers

def test_unique_columns():
    """测试没有重复列名的情况"""
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]

def test_duplicate_columns():
    """测试全部重复的列名"""
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]

def test_mixed_columns():
    """测试混合重复和唯一列名的情况"""
    cols = ["id", "name", "id", "name", "name"]
    expected = ["id", "name", "id.1", "name.1", "name.2"]
    assert dedupe_header(cols) == expected
def test_addition():
    """测试加法功能"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0