# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        queue = [root]

        res = []

        while queue:
            val_arr = []

            q_next_level = []

            for node in queue:
                val_arr.append(node.val)

                if node.left:
                    q_next_level.append(node.left)

                if node.right:
                    q_next_level.append(node.right)

            res.append(val_arr)

            queue = q_next_level  # 关键优化

        return res
