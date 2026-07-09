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
