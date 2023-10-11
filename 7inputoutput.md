# 字符串格式化

1. 引号前加 f，字符串内的变量用花括号
2. 花括号占位，后用 format 方法

```python
>>> votes=8824
>>> percentage=78.912
>>> f'{votes} YES votes {percentage}'
'8824 YES votes 78.912'
>>> '{} YES votes {}'.format(votes, percentage)
'8824 YES votes 78.912'
```

# 文件读写

为了避免忘记 open 之后忘记 close, 最好使用 with

```python
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
```
