# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        dic = {None: 0}

        def do(x):
            if not x:
                return 0
            l = do(x.left)
            r = do(x.right)
            res = max(l, r) + 1
            dic[x] = res
            return res

        do(root)
        cur = root
        while cur:
            he = dic[cur]
            lh = dic[cur.left]
            rh = dic[cur.right]
            if lh == rh:
                return cur

            if lh > rh:
                cur = cur.left
            elif lh < rh:
                cur = cur.right

