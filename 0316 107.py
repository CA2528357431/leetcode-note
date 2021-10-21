# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            res.append([x.val for x in queue])
            neo = []
            for x in queue:
                if x.left:
                    neo.append(x.left)
                if x.right:
                    neo.append(x.right)
            queue = neo
        return res[::-1]