# 二分法

[二分法](https://oi-wiki.org/basic/binary/#%E4%BA%8C%E5%88%86%E6%B3%95)
> 二分查找（英语：binary search），也称折半搜索（英语：half-interval search）、对数搜索（英语：logarithmic search），是用来在一个有序数组中查找某一元素的算法。

[二分查找](https://leetcode.cn/tag/binary-search/problemset/):二分查找也称折半查找

要求是有序数组，可升可降

时间复杂度： O(log n)

下面这个查找如果用直接遍历，时间复杂度就会是 O(n)，因此采取循环二分法

```python
class Solution:
    """        从升序整型数组中查找target的下标，不存在返回-1        
    [-1,0,3,5,9,12], target = 9, Output: 4
    [-1,0,3,5,9,12], target = 2, Output: -1
    """
    def search(self, nums: List[int], target: int) -> int:
        """        循环二分        """
        left,right=0,len(nums)-1
        while left<=right:
            mid=(right - left) //2 + left
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                return mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        """        递归二分法        """
        def rbs(nums, target, left, right):
            if left>right:
                return -1
            mid = (right - left) //2 + left
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return rbs(nums,target,mid+1,right)
            else:
                return rbs(nums,target,left,mid-1)

        return rbs(nums,target,0,len(nums)-1)
```

# Q&A

1. 中间数值的计算方式？

    `mid = (right - left) // 2 + left` 可以通过分数运算简化为 `mid = (right + left) // 2 `，然后在使用位运算替代除法 `mid = (right + left) >> 1 `，oi-wiki 中有解释道“n是非负数的时候，移位运算比整除法的机器指令少”

    但是看到官方解答和不少都不写直接相加再除二，而是先减除二再加，有热心的网友解释道，虽然两者在数学上相等，但是考虑到计算机存储器有上下界，直接相加溢出的可能性比先减除后加要大一点，比如c语言中int类型的最大值是 2147483647，再给它加一点点就溢出变成负数了。


2. while 是否要取等号？边界收缩条件？

    [704. Binary Search](https://leetcode.cn/problems/binary-search/)：取等、加一、减一

    [278. First Bad Version](https://leetcode.cn/problems/first-bad-version/)：取等、加一、减一；或者 不取等、加一、取中

    在278的官方解答也有评论在说这个事情，总之，不取等的时候边界收缩不一样

3. 题目中的条件中的数列是无序的，可以使用二分吗？

    如果使用排序后再二分的效率更高，可以直接对其进行排序再二分，如[两个数组间的距离值](https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/solution/liang-ge-shu-zu-jian-de-ju-chi-zhi-by-leetcode-sol/)
