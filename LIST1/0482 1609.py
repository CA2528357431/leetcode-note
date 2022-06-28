# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        cur = [root]
        c = 1
        while cur:
            neo = []
            for i in range(len(cur)):
                if i>0:
                    if c==1:
                        if cur[i-1].val>=cur[i].val:
                            return False
                    elif c==0:
                        if cur[i-1].val<=cur[i].val:
                            return False
                if cur[i].val%2!=c:
                    return False
                if cur[i].left:
                    neo.append(cur[i].left)
                if cur[i].right:
                    neo.append(cur[i].right)
            c = 1-c
            cur = neo
        return True