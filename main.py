import sys
from sim.io import read_file, write_result
from sim.similarity import duplication_rate

def main():
    if len(sys.argv) != 4:
        print("请使用: python main.py [orig_file] [suspect_file] [ans_file] 启动程序")
        sys.exit(1)
    orig_path, suspect_path, ans_path = sys.argv[1], sys.argv[2], sys.argv[3]
    orig_text = read_file(orig_path)
    suspect_text = read_file(suspect_path)
    rate = duplication_rate(orig_text, suspect_text)
    write_result(ans_path, rate)

if __name__ == "__main__":
    main()