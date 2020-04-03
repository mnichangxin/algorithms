# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            treeNodeTemp = root.left
            root.left = root.right
            root.right = treeNodeTemp

            self.mirrorTree(root.left)
            self.mirrorTree(root.right)

        return root


        