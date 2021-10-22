# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = -99999999
        def find(cur):
            nonlocal res
            if not cur:
                return 0
            l = max(0,find(cur.left))
            r = max(0,find(cur.right))
            value = cur.val+l+r
            res = max(res,value)
            # 在递归的同时更新结果将会很elegant
            return max(l,r)+cur.val
        find(root)
        return res


