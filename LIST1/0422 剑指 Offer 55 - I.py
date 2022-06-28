# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def find(cur):
            if not cur:
                return 0
            return max(find(cur.left),find(cur.right))+1
        return find(root)