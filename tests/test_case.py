# tests/test_cases.py
import os
from sim.similarity import duplication_rate


def test_same_text():
    orig = "今天天气晴朗，适合户外运动。"
    plag = "今天天气晴朗，适合户外运动。"
    assert round(duplication_rate(orig, plag), 2) == 100.00


def test_partial_modification():
    orig = "深度学习需要大量计算资源。"
    plag = "机器学习需要大量 GPU 资源。"
    rate = duplication_rate(orig, plag)
    # 预期大约在 50% 左右
    assert 30 <= rate <= 70


def test_completely_different():
    orig = "春天是万物复苏的季节。"
    plag = "量子物理研究微观粒子。"
    assert round(duplication_rate(orig, plag), 2) == 0.00


def test_empty_original():
    orig = ""
    plag = "这是一个测试句子。"
    assert round(duplication_rate(orig, plag), 2) == 0.00


def test_empty_both():
    orig = ""
    plag = ""
    # 两个空字符串 -> 认为是完全相同
    assert round(duplication_rate(orig, plag), 2) == 100.00


def test_single_char_same():
    orig = "A"
    plag = "A"
    assert round(duplication_rate(orig, plag), 2) == 100.00


def test_single_char_diff():
    orig = "A"
    plag = "B"
    assert round(duplication_rate(orig, plag), 2) == 0.00


def test_long_text():
    # 构造超长文本（1万字符）
    orig = "abcdefg" * (10000 // 7)
    plag = "abcdefg" * (10000 // 7)
    assert round(duplication_rate(orig, plag), 2) == 100.00


def test_long_text_with_diff():
    orig = "abcdefg" * (10000 // 7)
    plag = ("abcdefg" * (9999 // 7)) + "x"  # 最后有一个不同字符
    rate = duplication_rate(orig, plag)
    assert rate < 100 and rate > 90


def test_chinese_variation():
    orig = "“你好，”她说，“今天天气不错。”。"
    plag = "“你好！”他说，“今天天气很好。”"
    rate = duplication_rate(orig, plag)
    # 预期大约在 70-80%
    assert 70 <= rate <= 85


def test_polyphone_homograph():
    orig = "银行行长在银行门口行走。"
    plag = "银行行长在银行前行路。"
    rate = duplication_rate(orig, plag)
    # 预期大约在 70-85%
    assert 70 <= rate <= 85


def test_case_insensitivity():
    orig = "Hello World"
    plag = "hello world"
    assert round(duplication_rate(orig, plag), 2) == 100.00


def test_punctuation_ignored():
    orig = "Hello, world!!!"
    plag = "Hello world"
    assert round(duplication_rate(orig, plag), 2) == 100.00


def test_unicode_equivalence():
    # ﬁ (U+FB01) vs "fi"
    orig = "office"
    plag = "ofﬁce"
    assert round(duplication_rate(orig, plag), 2) == 100.00
