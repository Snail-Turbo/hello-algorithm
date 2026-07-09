# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        ans = 0

        def dfs(node) -> int:
            nonlocal ans  # 如果内部要赋值，必须 nonlocal

            if node is None:
                return -1

            left_max = dfs(node.left)
            right_max = dfs(node.right)

            current = left_max + right_max + 2

            if current > ans:
                ans = current

            return 1 + max(left_max, right_max)

        dfs(root)

        return ans
