class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    result = []

    def dfs(node: TreeNode):
        if not node:
            return

        dfs(node.left)

        result.append(node.val)

        dfs(node.right)

    return result


def preorderTraversal(root):
    result = []

    def dfs(node: TreeNode):
        if not node:
            return

        result.append(node.val)

        dfs(node.left)

        dfs(node.right)


def postorderTraversal(root):
    result = []

    def dfs(node: TreeNode):
        if not node:
            return

        dfs(node.left)

        dfs(node.right)

        result.append(node.val)
