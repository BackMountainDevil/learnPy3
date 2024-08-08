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

Counter 是 dict 的子类，其对象不能用在 dict 中作为键，否则会引发 `TypeError: unhashable type: 'Counter'`，这种情况可以将字符串排序后作为键，也可以用数组统计每个字符出现的次数，然后用数组做索引，参考 [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/solutions/520469/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/?envType=study-plan-v2&envId=top-interview-150)

# defaultdict

下面是一个计数例子，用来统计字符串中每个字符出现的次数

```python
s = 'mississippi'
d = {} # 空字典

for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

print(d)    # {'m': 1, 'i': 4, 's': 4, 'p': 2}

from collections import defaultdict
dd = defaultdict(int) # 空字典

for c in s:
    dd[c] += 1

print(dd)    # defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})
print(dd==d) # True
dd['x'] = 0  # 新增值为0的键值对
print(dd==d) # False
print(dd.items() == d.items())  # False
```

dict 里面没有出现的键，如果直接自加会报错，需要先判断存在与否再赋值，而 defaultdict(int) 里将未出现的键值对的默认值设为 0，所以可以直接自加，可以省心些。

判断 dict 和 defaultdict(int) 是否相等时，如果直接用 == 运算符，一般情况没有问题，除非中途有修改内容导致多余了一些值为 0 的键，比如上面代码最后加了一个 'x' 键值对。以下面的[例子](https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/)作为补充说明

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        ret = []
        if len(s) < lp:
            return ret
        cs, cp = defaultdict(int), defaultdict(int)
        for i in range(lp):
            c = p[i]
            cp[c] += 1
            c = s[i]
            cs[c] += 1
        if cs == cp:
            ret.append(0)
        for i in range(len(p), len(s)):
            c = s[i]
            cs[c] += 1
            cs[s[i - lp]] -= 1
            if cs[s[i - lp]] == 0:  #  删除值为0的键值对
                del cs[s[i - lp]]
            if cs == cp:
                ret.append(i - lp + 1)
        return ret
```

上面代码中，cp 统计了 p 中字母的出现次数，之后就不变了，用作对比，cs 随着滑动窗口的移动而变化，有时候会加入新字母，有时候会剔除旧字母，剔除的时候要判断是否为 0，从而删除这个键，不然多一个值为 0 的键会影响对比结果，从而导致错误。而使用 Counter 进行对比时存在 0 则不影响对比，下面的例子能够说明这个区别。

```python
from collections import Counter

s = "mississippi"
cs = Counter(s)
print(cs)               # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
cps = Counter(s)
print(cps, cs == cps)   # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1}) True
cps["x"] = 0    # py3.10 才加入富比较运算符，低版本时下面的比较会返回 False
print(cps, cs == cps)   # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1, 'x': 0}) True
cps["A"] += 1   # 不存在的键默认计数为 0
print(cps, cs == cps)   # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1, 'A': 1, 'x': 0}) False
```

此外，defaultdict(int) 之间不支持 in、> 等运算符，要比较范围建议使用 py3.10+ 的 Counter。

defaultdict(list) 的一个案例：[49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/solutions/520469/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/?envType=study-plan-v2&envId=top-interview-150)

