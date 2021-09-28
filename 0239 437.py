# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def do(cur, tar):
            mid = 0
            if not cur:
                return mid

            if cur.val == tar:
                mid += 1

            l = do(cur.left, tar - cur.val)
            r = do(cur.right, tar - cur.val)

            return mid + l + r

        cur = root
        res = 0
        stack = []

        while cur or stack:
            if not cur:
                cur = stack.pop().right
            else:
                res += do(cur, targetSum)
                stack.append(cur)
                cur = cur.left
        return res
