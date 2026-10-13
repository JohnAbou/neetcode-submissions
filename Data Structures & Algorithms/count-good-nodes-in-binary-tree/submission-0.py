# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, currentMax):
            if not node:
                return 0

            if node.val >= currentMax:
                count = 1
            else:
                count = 0

            newMax = max(node.val, currentMax)

            count += dfs(node.left, newMax)
            count += dfs(node.right, newMax)

            return count

        return dfs(root, root.val)