
# reduce

该函数可以将一个函数作用在一个序列的元素上，从头到尾，返回一个值。

例如下面的例子，求列表所有元素的亦或值。类似的还有求列表所有元素的与值、或值等。

```python
>>> from functools import reduce
>>> reduce(lambda x,y:x^y, [1, 2, 3, 4, 5, 1, 2, 3, 4])
5
```

其原理如下所示：

```python
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
```
