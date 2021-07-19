from Node import TreeNode
import collections

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        ret = (
            self.pathRootSum(root, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
        return ret

    def pathRootSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        ret = 0
        if root.val == targetSum:
            ret += 1
        ret += self.pathRootSum(root.left, targetSum - root.val) + self.pathRootSum(
            root.right, targetSum - root.val
        )
        return ret


class Solution2:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root, sumlist):
            if root is None:
                return 0
            sumlist = [num + root.val for num in sumlist] + [root.val]
            return (
                sumlist.count(sum) + dfs(root.left, sumlist) + dfs(root.right, sumlist)
            )

        return dfs(root, [])


# best
class Solution3:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # 对树做前序遍历同时做前缀和，同时记录祖先中的前缀和，在回溯时删除
        prefix_sum = collections.defaultdict(int)  # 记录路径中不同前缀和的数量
        prefix_sum[0] = 1  # 哨兵，没有节点时和为0
        pre = 0  # 从根节点到当前节点位置该路径的前缀和
        ans = 0

        def preOrder(root):
            nonlocal pre, prefix_sum, sum, ans
            if not root:
                return
            pre += root.val
            ans += prefix_sum[pre - sum]
            prefix_sum[pre] += 1

            preOrder(root.left)
            preOrder(root.right)

            prefix_sum[pre] -= 1
            pre -= root.val

        preOrder(root)
        return ans


# 这道题我看着先去看了560. 和为k的子数组 Subarray Sum Equals K，然后学到了prefixSum+HashTable的优化方式

# 之前写了半截的暴力解法

# 1.暴力解法
# 双层递归
# 核心在于：
# 每个node都要计算以它作为起点往下是否有path --> 这是一层递归
# 在考虑当前点为起点往下有没有path的时候，它的path可以往左也可以往右，于是要综合考虑 --> 这是另一层递归

# 那么我们可以写出第一层递归：


def pathSum(self, root: TreeNode, sum: int) -> int:
    """如果没有根节点，整个返回值应该为0，没有路径"""
    if not root:
        return 0
    """
        self.dfs(root, sum)：这个方法是判断以当前点为起点往下是否有path，也就是path的数量，返回值应该是0或1
        self.pathSum(root.left, sum)：对于左节点我依然要考虑以它为起点往下判断
        self.pathSum(root.right, sum)：同上，于是，此时的sum是不变化的，仍然为初始值
        """
    return (
        self.dfs(root, sum)
        + self.pathSum(root.left, sum)
        + self.pathSum(root.right, sum)
    )


# 那么对于计算当前点往下是否有path，就需要每一步update路径的和，题目是希望找到是否有路径总和为sum，那么为了简便，可以每一次都减去当前node.val，当遇到path==0的时候，就说明找到了一条路径，返回1，否则当root==None的时候，说明一直找不到路径，返回0


def dfs(self, root, path):
    if not root:
        return 0
    """每一次都要减去当前层的节点值"""
    path -= root.val
    """
        (1 if path==0 else 0)：说明找到了路径
        self.dfs(root.left, path) self.dfs(root.right, path)：
          此时path更新过，这是因为当前点既可以往左走找path，也可以往右走，是或的关系，只要有一边找到了路径，最终结果都会为1
        """
    return (
        (1 if path == 0 else 0) + self.dfs(root.left, path) + self.dfs(root.right, path)
    )


# 于是整体就能写出代码，一定要理解两个方法递归调用左孩子和右孩子的含义上的区别：


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        if not root:
            return 0
        return (
            self.dfs(root, sum)
            + self.pathSum(root.left, sum)
            + self.pathSum(root.right, sum)
        )

    def dfs(self, root, path):
        if not root:
            return 0
        path -= root.val
        return (
            (1 if path == 0 else 0)
            + self.dfs(root.left, path)
            + self.dfs(root.right, path)
        )


# 注意：但是这样的效率很低，因为递归层数过深，需要优化：

# 1.遇到subArray就考虑prefixSum和prefixSumArray，用hashtable
# 2.数组、链表考虑迭代遍历
# 3.树可左可右的就用递归代替迭代，并且递归结束之后要删掉当前层的tmp value
#   递归理解调用栈
#   并且：由于是递归而不是迭代，需要新的一个函数，且需要将prefixSum和prefixSumArray当作参数传入进去
# 2.prefixSum和prefixSumArray，+hashtable
# 类似560. 和为k的子数组 Subarray Sum Equals K，可以每次求出累加和，然后找到累加和和sum的差值，也就是距离为sum的路径，判断差值是否在我们用来保存每一个prefixSum的hashtable里，也类似2sum问题


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        prefixSumTree = {0: 1}
        self.count = 0

        prefixSum = 0
        self.dfs(root, sum, prefixSum, prefixSumTree)

        return self.count

    def dfs(self, root, sum, prefixSum, prefixSumTree):
        if not root:
            return 0
        prefixSum += root.val
        oldSum = prefixSum - sum
        if oldSum in prefixSumTree:
            self.count += prefixSumTree[oldSum]
        prefixSumTree[prefixSum] = prefixSumTree.get(prefixSum, 0) + 1

        self.dfs(root.left, sum, prefixSum, prefixSumTree)
        self.dfs(root.right, sum, prefixSum, prefixSumTree)

        """一定要注意在递归回到上一层的时候要把当前层的prefixSum的个数-1，类似回溯，要把条件重置"""
        prefixSumTree[prefixSum] -= 1
