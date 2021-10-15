# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res = 0

        def getsum(cur):
            nonlocal res

            if not cur:
                return 0
            l = getsum(cur.left)
            r = getsum(cur.right)

            res += abs(l - r)

            return l + r + cur.val

        getsum(root)
        return res