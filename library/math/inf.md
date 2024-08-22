math.inf 正无穷大的浮点数，负无穷大，使用 -math.inf.math.inf 相当于 float('inf') 的输出

```python
>>> a=2**32
>>> a
4294967296
>>> b=float('inf')
>>> b
inf
>>> a<b
True
>>> from math import inf
>>> b<inf
False
>>> a<inf
True
>>> b==inf
True
>>> inf>-inf
True
>>> 2**64<inf
Tru
>>> float('-inf')==-inf
True
>>> int('inf')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'inf'
```

