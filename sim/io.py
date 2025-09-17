# sim/io.py
from typing import Optional

def read_file(path: str) -> str:
    """
    以 utf-8 读取文本，忽略编码错误，返回原始字符串。
    """
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def write_result(path: str, value: float) -> None:
    """
    将浮点数写入结果文件，保留两位小数。
    覆盖写入（w）。
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write("{:.2f}".format(value))
