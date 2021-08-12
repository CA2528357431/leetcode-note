# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        big = max(p.val, q.val)
        small = min(p.val, q.val)

        cur = root

        while not small <= cur.val <= big:
            if cur.val > big:
                cur = cur.left
            else:
                cur = cur.right
        return cur