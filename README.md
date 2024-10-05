# 实用脚本

| 文件名              | 说明                                                      |
|---------------------|---------------------------------------------------------|
| AutoTencent.py      | 腾讯文档在线收集表定时自动抢填脚本                        |
| TestTencent.py      | 腾讯文档在线收集表选择题、填空题测试脚本                   |
| ParseCpp.py         | C++ 源代码文件简易解析脚本，可提取函数                     |
| ImageCompress.py    | PNG/JPG 图片定制尺寸压缩（极简）                            |
| SelfAttention.ipynb | 细致拆解， PyTorch 实现自注意力、多头、交叉、因果（掩码）注意力 |

## 使用方法

```bash
# 克隆仓库（SSH URL，推荐）
git clone --progress git@github.com:Dragon1573/Useful-Scripts.git

cd Useful-Scripts/

# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
./.venv/Scripts/activate

# 升级 pip
python -m pip install -U pip

# 安装依赖项
python -m pip install -U -r requirements.txt
```

## C++ 源代码文件解析脚本

此文件依赖 LLVM ，请参考 [进一步说明](./tools/README.md) 。
