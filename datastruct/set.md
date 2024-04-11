# 并查集

- [并查集基础](https://www.runoob.com/data-structures/union-find-basic.html)：三种优化方式
- [【算法与数据结构】—— 并查集 theSerein 2023-07-10](https://blog.csdn.net/the_zed/article/details/105126583)：两种优化方式
- [并查集 leetcode 题目](https://leetcode.cn/tag/union-find/problemset/)

并查集常用来解决连通性问题

n 个元素集合划分，最多划分为 n 个集合

1. 1xn 的数组，arr[i] 表示元素i所处集合的编号。编号相同代表属于同一集合。合并效率为 O(n)
2. 1xn 的数组（链表），arr[i] 表示元素i所处集合的前一个元素。

## 数组方法

```python
def find(x, f):
    # 查询元素所在的集合编号， x 是元素，f 是并查集
    return f[x]


def merge(x, y, f):
    # 合并元素 x 和元素 y 所属的集合，将xy的集合编号改成一样
    xid = find(x, f)
    yid = find(y, f)
    if xid != yid:
        # 将和y一组的，编号都修改为 x 的集合编号。只修改y的集合编号是错误的，把和y一组的遗漏了
        for i in range(len(f)):
            if f[i] == yid:
                f[i] = xid


n = 10  # 10个元素
f = [i for i in range(n)]  # 初始化并查集，每个元素都是不同的集合
edges = [[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]]
for x, y in edges:
    merge(x, y, f)
print(f"DEBUG f:{f}")  # 合并完成，集合编号一样的代表属于同一个集合
assert f[5] == f[7], "node 5 and 7 should be in the same set"

edges = [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]]
for x, y in edges:
    merge(x, y, f)
print(f"DEBUG f:{f}")
assert f[5] == f[9], "node5 and 9 should be in the same set"
```

## 链表方法

```python
# 合并效率为 O(h)，h 为树的高度
def find(x, parent):
    # 查找元素x所属的集合的根节点
    while x != parent[x]:
        x = parent[x]
    return x


def merge(x, y, parent):
    # 合并元素 x 和元素 y 所属的集合，将y的集合的根节点指向x的集合的根节点
    ix = find(x, parent)
    iy = find(y, parent)
    if ix != iy:
        parent[iy] = ix


n = 10  # 10个元素
parent = [i for i in range(n)]  # 初始化并查集，每个元素都是不同的集合
edges = [[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]]
for x, y in edges:
    merge(x, y, parent)
print(f"DEBUG parent:{parent}")
assert find(parent[5], parent) == find(parent[7], parent), "node 5 and 7 should be in the same set"
```

上面的树结构随机，还可以优化，将查找根节点的时间减少，那就要让树最好就两层，下面是结合路径压缩和层高压缩的代码，还有一种压缩是基于结点个数的

```python
def find(x):
    # 查找元素x所属的集合的根节点，并进行路径压缩
    # > 该算法存在一个缺陷：只有当查找了某个节点的代表元（教主）后，才能对该查找路径上的各节点进行路径压缩。换言之，第一次执行查找操作的时候是实现没有压缩效果的，只有在之后才有效
    if x != parent[x]:
        parent[x] = find(parent[x])  # 路径压缩
    return parent[x]


def merge(x, y):
    # 合并元素 x 和元素 y 所属的集合，将y的集合的根节点指向x的集合的根节点
    ix = find(x)
    iy = find(y)
    if ix != iy:
        if rank[ix] < rank[iy]:
            parent[ix] = iy
        elif rank[ix] > rank[iy]:
            parent[iy] = ix
        else:
            parent[ix] = iy
            rank[ix] += 1


n = 10  # 10个元素
parent = [i for i in range(n)]  # 初始化并查集，每个元素都是不同的集合
rank = [0] * n  # 初始时，每个集合的层数为0

edges = [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]]
for x, y in edges:
    merge(x, y)
print(f"DEBUG parent:{parent}")
assert find(parent[5]) == find(parent[9]), "node5 and 9 should be in the same set"
print(f"DEBUG num of sets - sum:{sum([parent[i]==i for i in range(n)])}")
# !!! 错误的方法，不能确保 par 中的都指向的是根结点
print(f"DEBUG Err num of sets - len:{len(set(parent))}")
# 需要注意这里 find 会修改 parent
print(f"DEBUG num of sets - sum:{sum([find(i)==i for i in range(n)])}")
```
