# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def deal(cur):
            if not cur:
                return
            cur.left,cur.right=cur.right,cur.left
            deal(cur.left)
            deal(cur.right)
        deal(root)
        return root