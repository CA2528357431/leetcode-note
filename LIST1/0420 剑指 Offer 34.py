# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:

        res = []
        sol = []

        def find(tar, cur):
            if not cur:
                return
            if not cur.left and not cur.right:
                if cur.val == tar:
                    sol.append(cur.val)
                    res.append(sol.copy())
                    sol.pop()
                return
            else:
                sol.append(cur.val)
                find(tar - cur.val, cur.left)
                find(tar - cur.val, cur.right)
                sol.pop()

        find(target, root)
        return res