# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        count = 0

        def find_target(node, current_sum):
            nonlocal count
            if node is None:
                return

            current_sum += node.val

            if current_sum == targetSum:
                count += 1

            find_target(node.left, current_sum)
            find_target(node.right, current_sum)

        def dfs(node):
            if node is None:
                return

            find_target(node, 0)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return count
