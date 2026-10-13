# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:

        # Quickly find each value's index in inorder
        inorder_index = {}

        for index, value in enumerate(inorder):
            inorder_index[value] = index

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            # No nodes exist inside this inorder range
            if left > right:
                return None

            # The next preorder value is the root
            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            # Find the root's position in inorder
            middle = inorder_index[root_value]

            # Build the left subtree first because preorder
            # visits: root -> left -> right
            root.left = build(left, middle - 1)
            root.right = build(middle + 1, right)

            return root

        return build(0, len(inorder) - 1)