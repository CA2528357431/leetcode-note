# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        cur=-99999999
        res=0
        queue = [root]
        i=0
        while queue:
            i+=1
            s=sum(x.val for x in queue)
            if s >cur:
                res=i
                cur=s
            neo = []
            for x in queue:
                if x.left:
                    neo.append(x.left)
                if x.right:
                    neo.append(x.right)
            queue = neo
        return res