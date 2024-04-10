"""
https://leetcode.cn/problems/binary-tree-preorder-traversal/solutions/461821/er-cha-shu-de-qian-xu-bian-li-by-leetcode-solution/
https://leetcode.cn/problems/binary-tree-postorder-traversal/solutions/431066/er-cha-shu-de-hou-xu-bian-li-by-leetcode-solution/
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""递归遍历 时间复杂度O(n)，空间复杂度 O(n)，n 是二叉树的节点数"""


def preorderTraversalRecursive(root: TreeNode) -> List[int]:
    # 二叉树的前序遍历（递归法）中左右
    def preorder(cur: TreeNode):
        if not cur:
            return
        res.append(cur.val)
        preorder(cur.left)
        preorder(cur.right)

    res = list()
    preorder(root)
    return res


def inorderTraversalRecursive(root: TreeNode) -> List[int]:
    # 二叉树的中序遍历（递归法）左中右
    def inorder(cur: TreeNode):
        if not cur:
            return
        inorder(cur.left)
        res.append(cur.val)
        inorder(cur.right)

    res = list()
    inorder(root)
    return res


def postorderTraversalRecursive(root: TreeNode) -> List[int]:
    # 二叉树的后序遍历（递归法）左右中
    def postorder(cur: TreeNode):
        if not cur:
            return
        postorder(cur.left)
        postorder(cur.right)
        res.append(cur.val)

    res = list()
    postorder(root)
    return res


"""迭代遍历"""


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    # 二叉树的前序遍历（迭代法）中左右，栈，时间复杂度O(n)，空间复杂度 O(n)，n 是二叉树的节点数
    ret = []
    if not root:
        return ret
    else:
        stack = [root]  # 栈，先进后出
        while stack:
            node = stack.pop()  # 弹出栈顶元素，即中先出
            ret.append(node.val)
            if node.right:  # 先进右子结点，这样出栈时才是中左右
                stack.append(node.right)
            if node.left:  # 再进左子结点
                stack.append(node.left)
        return ret


def preorderTraversalTemplate(root: Optional[TreeNode]) -> List[int]:
    # 二叉树的前序遍历（迭代法）中左右，时间复杂度O(n)，空间复杂度 O(n)
    ret = []
    if not root:
        return ret
    else:
        cur, stack = root, []
        while cur or stack:
            if cur:  # 根节点和左子结点入栈，把if换成while的话，把后面else去掉
                ret.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                tmp = stack.pop()  # 走向右子结点
                cur = tmp.right
        return ret


def preorderTraversalMirror(root: Optional[TreeNode]) -> List[int]:
    """
    二叉树的前序遍历（迭代法）中左右，时间复杂度O(n)，空间复杂度 O(1)

    新建临时节点，令该节点为 root；

    如果当前节点的左子节点为空，将当前节点加入答案，并遍历当前节点的右子节点；

    如果当前节点的左子节点不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点：

        如果前驱节点的右子节点为空，将前驱节点的右子节点设置为当前节点。然后将当前节点加入答案，并将前驱节点的右子节点更新为当前节点。当前节点更新为当前节点的左子节点。

        如果前驱节点的右子节点为当前节点，将它的右子节点重新设为空。当前节点更新为当前节点的右子节点。

    重复步骤 2 和步骤 3，直到遍历结束。
    """
    res = list()
    p1 = root
    while p1:
        p2 = p1.left
        if p2:
            while p2.right and p2.right != p1:
                p2 = p2.right
            if not p2.right:
                res.append(p1.val)
                p2.right = p1
                p1 = p1.left
                continue
            else:
                p2.right = None
        else:
            res.append(p1.val)
        p1 = p1.right

    return res


def inorderTraversalTemplate(root: TreeNode) -> List[int]:
    # 二叉树的中序遍历，时间复杂度O(n)，空间复杂度 O(n)
    ret = []
    if not root:
        return ret
    else:
        cur, stack = root, []  # 不能提前将root结点加入stack中
        while cur or stack:
            if cur:  # 先迭代访问最底层的左子树结点
                stack.append(cur)
                cur = cur.left
            else:
                tmp = stack.pop()
                ret.append(tmp.val)
                cur = tmp.right
        return ret


def inorderTraversalO2n(root: TreeNode) -> List[int]:
    # 二叉树的中序遍历，时间复杂度加倍： https://leetcode.cn/problems/binary-tree-inorder-traversal/solutions/25220/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
    stack, rst = [root], []
    while stack:
        i = stack.pop()
        if isinstance(i, TreeNode):
            stack.extend([i.right, i.val, i.left])
        elif isinstance(i, int):
            rst.append(i)
    return rst


def postorderTraversal(root: TreeNode) -> List[int]:
    # 后序遍历
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        # 中结点先处理
        result.append(node.val)
        # 左孩子先入栈
        if node.left:
            stack.append(node.left)
        # 右孩子后入栈
        if node.right:
            stack.append(node.right)
    # 将最终的数组翻转
    return result[::-1]


"""层序遍历"""


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    # 层序遍历，广度优先搜索（BFS）
    # https://leetcode.cn/problems/binary-tree-level-order-traversal/solutions/2361604/102-er-cha-shu-de-ceng-xu-bian-li-yan-du-dyf7/
    # 还可以使用 collections.deque 替代 list，其popleft()更快些
    res, queue = list(), list()
    if not root:
        return res
    else:
        queue.append(root)
        while queue:
            tmp = list()
            num = len(queue)
            for _ in range(num):  # queue 长度会变，提前确定长度
                node = queue.pop(0)  # 会消耗 O(n) 的时间
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)

    return res


def levelOrderDeque(root: Optional[TreeNode]) -> List[List[int]]:
    # 层序遍历，广度优先搜索（BFS），用 collections.deque 替代 list
    res = list()
    if not root:
        return res
    else:
        from collections import deque

        queue = deque([root])
        while queue:
            tmp = list()
            num = len(queue)
            for _ in range(num):  # queue 长度会变，提前确定长度
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)

    return res


def levelOrderRecursive(root: Optional[TreeNode]) -> List[List[int]]:
    # 层序遍历，递归法
    # https://leetcode.cn/problems/binary-tree-level-order-traversal/solutions/244292/tao-mo-ban-bfs-he-dfs-du-ke-yi-jie-jue-by-fuxuemin/
    # DFS 不是按照层次遍历的。为了让递归的过程中同一层的节点放到同一个列表中，在递归时要记录每个节点的深度 level。递归到新节点要把该节点放入 level 对应列表的末尾。
    def levelorder(cur, level):
        if not cur:
            return
        elif len(res) == level:
            res.append([])
        res[level].append(cur.val)
        levelorder(cur.left, level + 1)
        levelorder(cur.right, level + 1)

    res = list()
    levelorder(root, 0)
    return res


if __name__ == "__main__":
    print("""递归遍历测试""")
    print(preorderTraversalRecursive(None))  # []
    print(preorderTraversalRecursive(TreeNode(1)))  # [1]
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))  # [1,null,2,3]
    print(preorderTraversalRecursive(root))  # [1, 2, 3]
    print(inorderTraversalRecursive(root))  # [1, 3, 2]
    print(postorderTraversalRecursive(root))  # [3, 2, 1]

    print("""迭代遍历测试""")
    print(preorderTraversal(root))  # [1, 2, 3]
    print(preorderTraversalTemplate(root))
    print(preorderTraversalMirror(root))
    print(inorderTraversalTemplate(root))
    print(inorderTraversalO2n(root))

    print("""层序遍历测试""")
    root = TreeNode(
        3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))
    )  # [3,9,20,null,null,15,7]
    print(levelOrder(root))  # [[3], [9, 20], [15, 7]]
    print(levelOrderDeque(root))  # [[3], [9, 20], [15, 7]]
    print(levelOrderRecursive(root))  # [[3], [9, 20], [15, 7]]
