## cpp源代码文件解析工具

### llvm使用方法

本例中使用的版本是 [`LLVM-17.0.1-win64.exe`](https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.1/LLVM-17.0.1-win64.exe)

下载后，双击安装, 在python代码中设定对应路径即可，示例：

```python
clang.cindex.Config.set_library_file('D:/software/LLVM/bin/libclang.dll')
```
