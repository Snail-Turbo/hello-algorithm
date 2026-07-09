# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        count = 0

        # 一个用来枚举所有点，一个用来寻找合法路径

        def find_target(node, current_sum):
            nonlocal count
            if node is None:
                return

            current_sum += node.val

            if current_sum == targetSum:
                count += 1

            find_target(node.left, current_sum)
            find_target(node.right, current_sum)

        def dfs(node):  # 从上到下
            if node is None:
                return

            find_target(node, 0)  # 遍历每个作为root

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return count

    def pathSum_prefix(self, root: TreeNode, targetSum: int) -> int:
        # 前缀和计数
        prefix_count = {}
        prefix_count[0] = 1

        count = 0

        def dfs(node: TreeNode, current_sum):

            nonlocal count

            if node is None:
                return

            current_sum += node.val

            # target前缀和 处理
            current_diff = current_sum - targetSum
            if current_diff in prefix_count:
                count += prefix_count[current_diff]

            prefix_count[current_sum] = prefix_count.get(current_sum, 0)+1

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            prefix_count[current_sum] -= 1  # 需要退出来，因为，只能算当前路径才对

        dfs(root, 0)

        return count
