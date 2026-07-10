# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:

        if root is None:
            return []

        res = []
        queue = [root]

        while queue:
            val_array = []
            next_queue = []

            for node in queue:
                val_array.append(node.val)

                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            queue = next_queue
            if val_array:
                res.append(val_array[-1])

        return res

    def rightSideView(self, root: TreeNode) -> list[int]:

        if not root:
            return []

        q = [root]

        res = [root.val]

        while q:
            q_next_level = []
            val_arr = []

            for node in q:
                if node.left:
                    q_next_level.append(node.left)
                    val_arr.append(node.left.val)

                if node.right:
                    q_next_level.append(node.right)
                    val_arr.append(node.right.val)

            q = q_next_level

            if val_arr:
                res.append(val_arr[-1])

        return res
