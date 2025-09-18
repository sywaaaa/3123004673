def read_file(path: str) -> str:
    """读取文本文件，加入异常处理"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件未找到: {path}")
    except IOError as e:
        raise IOError(f"读取文件出错: {e}")

def write_result(path: str, rate: float):
    """写入结果文件，加入异常处理"""
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"{rate:.2f}%")
    except IOError as e:
        raise IOError(f"写入文件出错: {e}")
