# `__name__`

`__name__` 如果是当前程序调用这个属性，那么结果就是 `'__main__'`，如果是当前程序调用别的模块的name属性，结果的就是对应模块的名称

```python
>>> __name__
'__main__'
>>> from http import server
>>> server.__name__
'http.server'
```

在编写正式代码时，建议将运行代码都放到 main 下

```python
if __name__ == "__main__":
    # code
```

# import

`from pygame import *` 这种方式会导入所有名称不以下划线（_）开头的函数，缺点是可能会覆盖已经定义的名称，还可能引发 flake8 的温馨提示

# dir()

`dir()` 用于查找模块定义的函数和变量，但不包括 builtins 定义的内置函数和变量
