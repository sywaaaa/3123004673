import os
import subprocess

# 原文件路径
orig_file = r"E:\软件工程作业\第二次作业\测试文本\orig.txt"

# 需要对比的文件
suspect_files = [
    r"E:\软件工程作业\第二次作业\测试文本\orig_0.8_add.txt",
    r"E:\软件工程作业\第二次作业\测试文本\orig_0.8_del.txt",
    r"E:\软件工程作业\第二次作业\测试文本\orig_0.8_dis_1.txt",
    r"E:\软件工程作业\第二次作业\测试文本\orig_0.8_dis_10.txt",
    r"E:\软件工程作业\第二次作业\测试文本\orig_0.8_dis_15.txt",
]

# 遍历每个文件并执行 main.py
for suspect in suspect_files:
    # ans_file 命名规则（比如 orig_0.8_add_ans.txt）
    ans_file = suspect.replace(".txt", "_ans.txt")

    cmd = ["python", "main.py", orig_file, suspect, ans_file]
    print("运行命令:", " ".join(cmd))

    # 执行命令
    subprocess.run(cmd, check=True)

print("全部执行完成！")
