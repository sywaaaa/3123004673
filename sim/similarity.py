# sim/similarity.py
from .preprocess import normalize_text

def duplication_rate(orig_text: str, suspect_text: str) -> float:
    """
    基于编辑距离的重复率计算。
    - 插入、删除、替换算一步操作
    - 相似度 = (1 - 编辑距离 / max(len(orig), len(suspect))) * 100
    """

    a = normalize_text(orig_text)
    b = normalize_text(suspect_text)

    # 边界情况
    if not a and not b:
        return 100.0
    if not a or not b:
        return 0.0

    n, m = len(a), len(b)

    # 初始化 DP 表
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # 动态规划计算编辑距离
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,       # 删除
                dp[i][j - 1] + 1,       # 插入
                dp[i - 1][j - 1] + cost # 替换 / 不变
            )

    distance = dp[n][m]
    similarity = (1 - distance / max(n, m)) * 100
    return round(similarity, 2)
