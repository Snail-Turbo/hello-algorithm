# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 关键思路：
# 1. 初始化 answer 为 min_impossible
# 2. def dfs(node) -> int:
# 3. nonlocal answer
# 4.


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 左子树链(或空) -> 拐点 -> 右子树链(或空)
        if root is None:
            return 0

        min_impossible = -10**18
        answer = min_impossible  # 【易错】 answer初始应该初始化为 不可能的小

        def dfs(node) -> int:
            nonlocal answer

            if node is None:
                return 0

            current_val = node.val

            # 如果子树 局部最优解小于0，可以不取子树，左右均有可能不取
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            current_max = left_max + right_max + current_val

            if current_max > answer:
                answer = current_max

            # 【易错】 返回给父节点的时候，只能传一条子链
            if left_max > right_max:
                return current_val + left_max

            return current_val + right_max

        dfs(root)

        return answer
