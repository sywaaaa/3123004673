# sim/similarity.py
from difflib import SequenceMatcher
from .preprocess import normalize_text
from typing import Tuple

def matched_length(a: str, b: str) -> int:
    """
    返回 a 与 b 的匹配字符数量（使用 difflib 的 matching blocks）。
    """
    sm = SequenceMatcher(None, a, b)
    # get_matching_blocks() 返回若干 (i,j,n)，最后一个是 (len(a),len(b),0)
    return sum(block.size for block in sm.get_matching_blocks())

def duplication_rate(orig_text: str, suspect_text: str) -> float:
    """
    计算重复率（百分比），保留原文长度为分母：
      rate = matched_chars / len(orig_normalized) * 100
    若原文长度为 0，返回 0.0
    """
    a = normalize_text(orig_text)
    b = normalize_text(suspect_text)
    if not a:
        return 0.0
    matched = matched_length(a, b)
    return matched / len(a) * 100.0
