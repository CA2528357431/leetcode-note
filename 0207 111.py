# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.right and not root.left:
            return 1
        elif not root.left:
            r = self.minDepth(root.right)
            return r+1
        elif not root.right:
            l = self.minDepth(root.left)
            return l+1
        else:
            l = self.minDepth(root.left)
            r = self.minDepth(root.right)
            return 1+min(l,r)