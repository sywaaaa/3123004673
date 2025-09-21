# 文本相似度检测工具

本项目实现了一个基于 **编辑距离** 的文本相似度计算工具，针对长文本进行了 空间优化（滚动数组），在大文本下仍能高效计算。可以通过命令行比较两篇文本的相似度，并将结果写入指定文件。

## 使用方式

命令格式：

```bash
python main.py [orig_file] [suspect_file] [ans_file]
```

参数说明：

* `orig_file`：原文文件路径
* `suspect_file`：待检测文件路径
* `ans_file`：结果输出文件路径

## 示例

假设有以下两个文本文件：

* `orig.txt`

  ```
  今天真是个天气晴朗的日子
  ```

* `suspect.txt`

  ```
  今天是个好日子
  ```

执行命令：

```bash
python main.py orig.txt suspect.txt result.txt
```

运行后，`result.txt` 会输出两段文本的相似度，例如：

```
66.67%
```

## 文件结构

```
project/
│── sim/
│   ├── __init__.py
│   ├── io.py             # 文件读写
│   ├── preprocess.py     # 文本预处理
│   └── similarity.py     # 相似度计算
|── 测试文本
|── tests/
|   |──__init__.py
|   |──__test_case__.py   #边缘测试样例
│── main.py               # 主程序入口
│── test_long_high_similarity.py          # 性能测试入口
│── test.py 测试文本测试入口
│── README.md
```
