class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        answer = 0

        def dfs(node: TreeNode, depth: int):
            if not node:
                return

            if not node.left and not node.right and depth > answer:
                answer = depth
                return

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

            return

        dfs(root, 1)

    def maxDepth(self, root: TreeNode) -> int:
        # 自顶向下，求每一个到 叶子 路径长度
        if root is None:
            return 0

        answer = 0

        def dfs(node, depth):
            nonlocal answer

            if node is None:
                return

            if node.left is None and node.right is None:  # 从上到下的记录终止条件，叶子节点无子节点
                if depth > answer:
                    answer = depth
                return

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 1)

        return answer

    def maxDepth2(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            return max(dfs(node.left), dfs(node.right)) + 1

    def maxDepth2(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0

            return 1 + max(dfs(node.left), dfs(node.right))

        return dfs(root)

    def max_depth(self, root: list) -> int:
        n = len(root)

        def dfs(index):
            if index >= n or root[index] is None:
                return 0

            return 1 + max(dfs(2*index+1), dfs(2*index+2))

        return dfs(0)


def seserialize(root_string: str):
    root_string = root_string.strip()

    if root_string == "[]":
        return []

    raw_array = root_string[1:-1].split(",")

    root_array = []

    for raw in raw_array:
        raw = raw.strip()

        if raw in ('null', 'None'):
            root_array.append(None)
        else:
            root_array.append(int(raw))

    return root_array


root = " [3,9,20,null,null,15,7]"

root_array = seserialize(root)
print(root_array)

so = Solution()

print(so.max_depth(root_array))
