https://docs.python.org/zh-cn/3.12/library/functions.html

# bin

`bin(x)`:     将一个整数 x 转换为带前缀 "0b" 的二进制数字符串。

```python
>>> bin(6)
'0b110'
>>> bin(-6)
'-0b110'
>>> bin(6)[2:]  # 非负数可以这样去掉 0b 前缀
'110'
>>> bin(-6)[2:]  # ！！！负数这样去会有问题
'b110'
>>> format(14, '#b'), format(14, 'b')   # 注意看 '#b' 输出带 0b, 'b' 输出不带 0b
('0b1110', '1110')
>>> f'{14:#b}', f'{14:b}'      # 注意看 '#b' 输出带 0b, 'b' 输出不带 0b
('0b1110', '1110')
```

#  int

`class int(number=0, /)`、`class int(string, /, base=10)`: 返回一个由字符串转换过来的整数对象。没有参数默认返回 0。

> 10--35 的值可以用 a 到 z (或 A 到 Z) 来表示。 默认的 base 为 10。 允许的基数为 0 和 2--36。 对于基数 2, 8 和 16 来说字符串前面还能加上可选的 0b/0B, 0o/0O 或 0x/0X 前缀，就像代码中的整数字面值那样。 对于基数 0 来说，字符串会以与 代码中的整数字面值 类似的方式来解读，即实际的基数将由前缀确定为 2, 8, 10 或 16。 基数为 0 还会禁用前导的零: int('010', 0) 将是无效的，而 int('010') 和 int('010', 8) 则是有效的

```python
>>> int(123.45) # 向零取整
123
>>> int('123')  # 字符串转整数
123
>>> int('   -12_345\n')
-12345
>>> int('   -12-345\n')
ValueError: invalid literal for int() with base 10: '   -12-345\n'
>>> int('   12-345\n')
ValueError: invalid literal for int() with base 10: '   12-345\n'
>>> int('   12+345\n')
ValueError: invalid literal for int() with base 10: '   12+345\n'
>>> int('FACE', 16)  # 16进制字符串转整数，要指定基数，不指定按照10进制处理会出错
64206
>>> int('0xface', 0)
64206
>>> int('01110011', base=2) # 2进制字符串转整数，要指定基数
115
>>> int('0b0101', 2)
5
```

向上取整：math.ceil(a/b)、（a+b-1)//b

向下取整：math.floor(a/b)、整除"a//b"

向0取整：int()

四舍五入：round()——奇数向远离0取整，偶数去尾取整；或言之：奇数进位，偶数去尾

# map

`map(function, iterable, *iterables)`: 返回一个将 function 应用于 iterable 的每一项，并产生其结果的迭代器。

```python
>>> i=map(lambda x: x**2, [1, 2, 3, 4])
>>> i
<map object at 0x76831c11e020>
>>> type(i)
<class 'map'>
>>> next(i)
1
>>> next(i)
4
>>> next(i)
9
>>> next(i)
16
>>> i
<map object at 0x76831c11e020>
>>> next(i)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

输入多个数字数常用其来将输入的字符转为数字

```python
nums=list(map(int, input().split()))
```

# reversed

`reversed(seq)`: 返回一个反向的 iterator。 不是返回反转好的对象

```python
>>> s='abcdefg'
>>> reversed(s)
<reversed object at 0x71551e0b0df0>
>>> list(reversed(s))   # 反转字符串建议用 s[::-1]
['g', 'f', 'e', 'd', 'c', 'b', 'a']
```
