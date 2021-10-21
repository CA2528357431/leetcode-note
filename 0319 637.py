# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            res.append(sum([x.val for x in queue])/len(queue))
            neo = []
            for x in queue:
                if x.left:
                    neo.append(x.left)
                if x.right:
                    neo.append(x.right)
            queue = neo
        return res