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
        result = []

        while queue:
            val_array = []
            next_queue = []

            for current_node in queue:
                val_array.append(current_node.val)

                if current_node.left:
                    next_queue.append(current_node.left)

                if current_node.right:
                    next_queue.append(current_node.right)

            result.append(val_array)

            queue = next_queue

        return result
