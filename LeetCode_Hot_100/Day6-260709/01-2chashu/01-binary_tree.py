"""
当前下标：i
左孩子：2 * i + 1
右孩子：2 * i + 2

父节点：(i - 1) // 2
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def create_2_tree(self, tree_list):
        if len(tree_list) == 0:
            return None

        root_node = TreeNode(tree_list[0])
        queue = [root_node]

        index = 1

        while queue and index < len(tree_list):

            current_node = queue.pop(0)

            if index < len(tree_list) and tree_list[index] is not None:
                current_node.left = TreeNode(tree_list[index])
                queue.append(current_node.left)

            index += 1

            if index < len(tree_list) and tree_list[index] is not None:
                current_node.right = TreeNode(tree_list[index])
                queue.append(current_node.right)

            index += 1

        return root_node


def seserialize(tree_str: str):
    tree_str = tree_str.strip()

    if tree_str == "[]":
        return []

    raw_array = tree_str[1:-1].split(",")

    tree_array = []

    for raw in raw_array:
        node_val = raw.strip()

        if node_val in ("null", "None"):
            tree_array.append(None)

        else:
            tree_array.append(int(node_val))

    return tree_array
