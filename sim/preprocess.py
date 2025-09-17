# sim/preprocess.py
import unicodedata
import re

def normalize_text(text: str) -> str:
    """
    规范化文本以便进行字符级匹配：
    - NFKC 归一化
    - 去掉 BOM
    - 小写化（对拉丁文字）
    - 删除除字母数字和 CJK 统一汉字之外的字符（去除标点、空格等）
    返回处理后的字符串（不含空白和标点）。
    """
    if text is None:
        return ""
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\ufeff", "")
    text = text.lower()
    # 保留字母数字下划线（\w）以及中文 Unicode 范围 \u4e00-\u9fff
    # 其余替换为空
    text = re.sub(r"[^\w\u4e00-\u9fff]+", "", text)
    return text
