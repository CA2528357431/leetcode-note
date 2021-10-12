# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        if root == p or root == q:
            return root
        # 如果在root

        lf = self.lowestCommonAncestor(root.left, p, q)
        rf = self.lowestCommonAncestor(root.right, p, q)

        if lf and rf:
            return root
        # 如果左右各一个
        elif rf:
            return rf
        elif lf:
            return lf
        # 如果只有一侧有