# sim/similarity.py
from .preprocess import normalize_text

def duplication_rate(orig_text: str, suspect_text: str) -> float:
    """
    基于编辑距离的重复率计算（滚动数组优化）。
    - 插入、删除、替换算一步操作
    - 相似度 = (1 - 编辑距离 / max(len(orig), len(suspect))) * 100
    - 空对空 -> 100%，空对非空 -> 0%
    """

    a = normalize_text(orig_text)
    b = normalize_text(suspect_text)

    if not a and not b:
        return 100.0
    if not a or not b:
        return 0.0

    n, m = len(a), len(b)

    # 确保 b 是较短的那个，减少空间
    if n < m:
        a, b = b, a
        n, m = m, n

    # 只保留两行
    prev_row = list(range(m + 1))
    curr_row = [0] * (m + 1)

    for i in range(1, n + 1):
        curr_row[0] = i
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            curr_row[j] = min(
                prev_row[j] + 1,        # 删除
                curr_row[j - 1] + 1,    # 插入
                prev_row[j - 1] + cost  # 替换 / 不变
            )
        prev_row, curr_row = curr_row, prev_row  # 滚动切换

    distance = prev_row[m]
    similarity = (1 - distance / max(len(a), len(b))) * 100
    return round(similarity, 2)
