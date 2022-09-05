# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 1
        cur = [root]
        dic = {root: 0}
        while cur:

            nxt = []
            neodic = {}
            pre = -1
            post = -1
            for x in cur:
                if x.left:
                    nxt.append(x.left)
                    neodic[x.left] = dic[x] * 2 + 1
                    if pre < 0:
                        pre = neodic[x.left]
                    post = neodic[x.left]
                if x.right:
                    nxt.append(x.right)
                    neodic[x.right] = dic[x] * 2 + 2
                    if pre < 0:
                        pre = neodic[x.right]
                    post = neodic[x.right]
            cur = nxt
            dic = neodic

            if pre < 0:
                return res
            else:
                res = max(res, post - pre + 1)

        return res