# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        cur=[root]
        while True:
            nxt=[]
            for x in cur:
                if x.left:
                    nxt.append(x.left)
                if x.right:
                    nxt.append(x.right)
            if not nxt:
                break
            cur=nxt
        return cur[0].val