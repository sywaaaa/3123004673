import sys
from sim.io import read_file, write_result
from sim.similarity import duplication_rate

def main():
    if len(sys.argv) != 4:
        print("请使用: python main.py [orig_file] [suspect_file] [ans_file] 启动程序")
        sys.exit(1)

    orig_path, suspect_path, ans_path = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        orig_text = read_file(orig_path)
        suspect_text = read_file(suspect_path)
    except Exception as e:
        print(f"读取文件出错: {e}")
        sys.exit(1)

    try:
        rate = duplication_rate(orig_text, suspect_text)
    except Exception as e:
        print(f"计算重复率出错: {e}")
        sys.exit(1)

    try:
        write_result(ans_path, rate)
    except Exception as e:
        print(f"写入结果文件出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
