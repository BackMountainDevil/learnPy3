# 输入

input() 会从输入中读取一行，将其转换为字符串（除了末尾的换行符）并返回。整形和浮点形需要额外转换。

输入一维数组

```python
# 第一行给定一个整数n，表示数组大小，第二行给定n个整数，整数之间用空格隔开
# 4
# 1 4 6 3
n = int(input())    # 整数n
arr = list(map(int, input().split()))   # 用 map 将元素都变成整形，split 默认是空格分隔
```

输入二维数组

```python
# 第一行输入两个整数n,m用空格隔开
# 接下来n行，每行输入m个整数，用,隔开
# 3 4
# 1,1,1,0
# 0,0,1,1
# 1,0,1,1
n, m = map(int, input().split())
arr = []    # 初始化空数组
for i in range(n):  # 这里不检查是否输入的是 m 个
    row = list(map(int, input().split(',')))    # 题目说逗号分隔，split 参数要填逗号
    arr.append(row)
```

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
