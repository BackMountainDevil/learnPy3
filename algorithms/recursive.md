# 递归

递归的常见结构

```python
def fib(n):
    if n<3:
        return n
    else:
        return fib(n-1)+fib(n-2)
```

确定边界条件之后，就是递归表达式。递归表达式一般来说作为返回值，然而也可以不在返回值的位置，如[递归倒置单链表](https://leetcode.cn/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-by-leetcode-solution-d1k2/)
