import random
import time
from sim.io import read_file, write_result
from sim.similarity import duplication_rate


def generate_long_chinese_text(base_sentences, target_length=5000):
    """将基础句子重复拼接生成长文本"""
    text = ""
    while len(text) < target_length:
        text += random.choice(base_sentences)
    return text[:target_length]


def generate_high_similarity_text(orig_text, modification_ratio=0.02):
    """在原文本上进行少量修改生成高相似度文本"""
    plag_list = list(orig_text)
    num_modifications = int(len(orig_text) * modification_ratio)
    for _ in range(num_modifications):
        idx = random.randint(0, len(orig_text) - 1)
        plag_list[idx] = random.choice("的一了是有在和不")
    return "".join(plag_list)


def save_text(path: str, text: str) -> None:
    """保存长文本到文件，避免 write_result 浮点限制"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    base_sentences = [
        "今天早上阳光明媚，空气清新，适合去公园散步。",
        "小明在图书馆认真阅读，学习气氛非常浓厚。",
        "春天的花园里，百花齐放，蝴蝶在花间飞舞。",
        "夜晚的星空灿烂，微风拂面，让人心情愉快。",
        "电脑科学的发展日新月异，人工智能改变了生活。"
    ]

    # 1. 生成原文文本并保存
    orig_text = generate_long_chinese_text(base_sentences, target_length=5000)
    save_text("orig.txt", orig_text)

    # 2. 生成高相似度文本并保存
    suspect_text = generate_high_similarity_text(orig_text)
    save_text("suspect.txt", suspect_text)

    # 3. 从文件读取文本
    orig_text = read_file("orig.txt")
    suspect_text = read_file("suspect.txt")

    # 4. 计算相似度
    print("开始大文本高相似度测试...")
    start_time = time.time()
    rate = duplication_rate(orig_text, suspect_text)
    end_time = time.time()

    print(f"文本长度: {len(orig_text)}")
    print(f"相似度: {rate:.2f}%")
    print(f"耗时: {end_time - start_time:.2f} 秒")

    # 5. 保存相似度结果到文件（使用 write_result）
    write_result("ans.txt", rate)

    # 可选验证
    assert rate > 90, f"相似度过低: {rate:.2f}%"


if __name__ == "__main__":
    main()
