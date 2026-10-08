# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            rob_node = node.val + left[1] + right[1]

            skip_node = (
                max(left[0], left[1]) +
                max(right[0], right[1])
            )

            return [rob_node, skip_node]

        result = dfs(root)

        return max(result)
        