# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        if not root:
            return []

        sol = [root.val]
        res = []
        def do(cur,tar):
            if tar == 0 and not cur.left and not cur.right:
                res.append(sol.copy())
            if cur.left:
                sol.append(cur.left.val)
                l = do(cur.left, tar - cur.left.val)
                sol.pop()
            if cur.right:
                sol.append(cur.right.val)
                r = do(cur.right, tar - cur.right.val)
                sol.pop()
        do(root,targetSum-root.val)
        return res
        '''

        if not root:
            return []

        sol = []
        res = []

        def do(cur, tar):
            if not cur:
                return
            sol.append(cur.val)
            if not cur.left and not cur.right:
                if tar - cur.val == 0:
                    res.append(sol.copy())

            else:
                do(cur.left, tar - cur.val)
                do(cur.right, tar - cur.val)
            sol.pop()

        do(root, targetSum)
        return res