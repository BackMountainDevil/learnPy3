https://docs.python.org/zh-cn/3/library/bisect.html

# bisect_left

`bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)`
> 在 a 中找到 x 合适的插入点以维持有序。参数 lo 和 hi 可以被用于确定需要考虑的子集；默认情况下整个列表都会被使用。如果 x 已经在 a 里存在，那么插入点会在已存在元素之前（也就是左边）。如果 a 是列表（list）的话，返回值是可以被放在 list.insert() 的第一个参数的。
>
> 在 3.10 版本发生变更: 增加了 key 形参。

`bisect.bisect_right(a, x, lo=0, hi=len(a), *, key=None)` 则是找不是 x 的最小右边界

```python
>>> import bisect
>>> a = [1, 3, 5, 5, 7, 9]
>>> bisect.bisect_left(a, 0)
0
>>> bisect.bisect_left(a, 3)
1
>>> bisect.bisect_left(a, 5)
2
>>> bisect.bisect_left(a, 6)
4
>>> bisect.bisect_left(a, 10)
6

>>> bisect.bisect_right(a, 0)
0
>>> bisect.bisect_right(a, 3)
2
>>> bisect.bisect_right(a, 5)
4
>>> bisect.bisect_right(a, 6)
4
>>> bisect.bisect_right(a, 10)
6
```


