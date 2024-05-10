# permutations combinations

math.perm(n, k)、math.comb(n, k) 分别计算n个元素中取k个元素的排列数和组合数。

```python
>>> from itertools import permutations, combinations
>>> perms = permutations([1,2,3], 2) # 求所有的排列
>>> [p for p in perms]
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
>>> combins = combinations([1,2,3], 2)  # 求所有的组合
>>> [c for c in combins]
[(1, 2), (1, 3), (2, 3)]
```

自己用代码实现列出排列、组合的全部情况：

```python
def combinations(lst, n):
    """
    Returns all possible combinations of n elements from lst.
    >>> combinations([1, 2, 3], 2)
    [[1, 2], [1, 3], [2, 3]]

    >>> combinations([1, 2, 3], 3)
    [[1, 2, 3]]

    >>> combinations([1, 2, 3], 0)
    [[]]
    """
    if n == 0:
        return [[]]
    else:
        combs = []
        for i in range(len(lst)):
            rest = lst[i + 1 :]
            for c in combinations(rest, n - 1):
                combs.append([lst[i]] + c)
        return combs


def permutations(lst, n):
    """
    Returns all possible permutations of n elements from lst.
    >>> permutations([1, 2, 3], 2)
    [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]

    >>> permutations([1, 2, 3], 3)
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    >>> permutations([1, 2, 3], 0)
    [[]]
    """
    if n == 0:
        return [[]]
    else:
        perms = []
        for i in range(len(lst)):
            rest = lst[:i] + lst[i + 1 :]
            for p in permutations(rest, n - 1):
                perms.append([lst[i]] + p)
        return perms


def combinations_yield(m, n):
    """生成从m个自然数里取n个数的所有可能组合

    >>> print(combinations_yield(4, 4))
    [[1, 2, 3, 4]]
    >>> print(combinations_yield(4, 3))
    [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    >>> print(combinations_yield(4, 2))
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    >>> print(combinations_yield(4, 1))
    [[1], [2], [3], [4]]
    """

    def helper(data, r):
        if r == 0:
            yield []
        else:
            for i in range(len(data)):
                for c in helper(data[i + 1 :], r - 1):
                    yield [data[i]] + c

    data = list(range(1, m + 1))  # 生成1到m的数字列表
    return list(helper(data, n))
```
