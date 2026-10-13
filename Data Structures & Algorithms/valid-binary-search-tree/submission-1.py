# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, minimum, maximum):
            if not node:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False

            validateLeft = dfs(node.left, minimum, node.val)
            validateRight = dfs(node.right, node.val, maximum)

            return validateLeft and validateRight

        return dfs(root, float('-inf'), float('inf'))

