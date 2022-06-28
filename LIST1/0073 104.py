# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = 0
        queue = [root]
        while queue:
            res+=1
            neo = []
            for x in queue:
                if x.left:
                    neo.append(x.left)
                if x.right:
                    neo.append(x.right)
            queue = neo
        return res