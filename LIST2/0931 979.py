# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        diccoin = {None: 0}

        def coin(cur):
            if not cur:
                return 0
            res = coin(cur.left) + coin(cur.right) + cur.val
            diccoin[cur] = res
            return res

        dicnum = {None: 0}

        def num(cur):
            if not cur:
                return 0
            res = num(cur.left) + num(cur.right) + 1
            dicnum[cur] = res
            return res

        coin(root)
        num(root)
        # print(len(dicnum))
        # print(len(diccoin))

        cnt = 0

        def do(cur):
            if not cur:
                return
            nonlocal cnt
            lc = diccoin[cur.left]
            ln = dicnum[cur.left]
            rc = diccoin[cur.right]
            rn = dicnum[cur.right]
            # cnt+=abs((lc+rc+cur.val)-(1+ln+rn))
            cnt += abs(lc - ln)
            cnt += abs(rc - rn)
            do(cur.left)
            do(cur.right)

        do(root)

        return cnt
