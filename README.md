# 文本相似度检测工具

本项目实现了一个基于 **编辑距离（Levenshtein Distance）** 的文本相似度计算函数，用于计算两段文本之间的重复率。

## 功能特点

* 预处理文本（去除多余空格、统一大小写等）。
* 使用编辑距离衡量文本差异。
* 输出重复率（0% \~ 100%）。
* 提供丰富的单元测试（包含边界情况）。

## 目录结构

```
project/
│── sim/
│   ├── __init__.py
│   ├── preprocess.py      # 文本预处理
│   └── similarity.py      # 相似度计算
│── tests/
│   └── test_case.py       # 单元测试
│── requirements.txt
│── README.md
```

## 安装

建议使用虚拟环境：

```bash
python -m venv venv
source venv/bin/activate  # Linux / MacOS
venv\Scripts\activate     # Windows
```

安装依赖：

```bash
pip install -r requirements.txt
```

## 使用示例

```python
from sim.similarity import duplication_rate

orig = "今天真是个天气晴朗的日子"
plag = "今天是个好日子"

rate = duplication_rate(orig, plag)
print(f"相似度: {rate:.2f}%")  # 输出大约 66.67%
```

## 运行测试

```bash
pytest -v
```


