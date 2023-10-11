[collections --- 容器数据类型](https://docs.python.org/zh-cn/3/library/collections.html)

# deque
双向队列

# Counter 计数器

方便一行代码统计各个字符的频数

```python
from collections import Counter

string = "this is a string"
times = Counter(string) # 统计每种字符出现的次数，包含空格
for k, v in times.items():
    print(k, v)
```

[赎金信 方法一：字符统计 leetcode](https://leetcode.cn/problems/ransom-note/solution/shu-jin-xin-by-leetcode-solution-ji8a/)：我用的 Counter 之后在遍历其对象，但是官方解答连遍历都省去了，直接相减 + not，给我整不会了

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
```

前者(ransomNote) 减去 后者(magazine)，可以类比为集合做减法，如果某字符数量一样，减掉了数量为0,需要注意这时候结果中不会保留0，而是直接删除这个字符的计数；如果某字符的计数在前者比后者小，相减结果是复数，但是根据库文档里面一句注释“subtract (keeping only positive counts)”，也就是说减法的时候非正数都会被删除；如果某些字符前者有后者没有，就像集合一样结果中也是没有的。对一个空的 Counter 对象做非运算，结果为真，对非空的做非运算结果为假

```python
>>> from collections import Counter
>>> Counter("a")-Counter("aabc")
Counter()
>>> Counter("a")-Counter("abc")
Counter()
>>> Counter("a")-Counter("bc")
Counter({'a': 1})
>>> not Counter("a")-Counter("aabc")
True
>>> not Counter("a")-Counter("abc")
True
>>> not Counter("a")-Counter("bc")
False
```
