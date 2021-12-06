# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        dics = {None: False}
        dice = {None: False}

        def have(root, x):
            if not root:
                return False
            if root.val == x:
                if x == startValue:
                    dics[root] = True
                else:
                    dice[root] = True
                return True
            judge = have(root.left, x) or have(root.right, x)
            if x == startValue:
                dics[root] = judge
            else:
                dice[root] = judge
            return judge

        def findroot(root):
            if root.left in dice and root.left in dics and dics[root.left] and dice[root.left]:
                return findroot(root.left)
            elif root.right in dice and root.right in dics and dics[root.right] and dice[root.right]:
                return findroot(root.right)
            return root

        have(root, startValue)
        have(root, destValue)
        mid = findroot(root)
        res = []

        cur = mid
        while cur.val != startValue:
            if cur.left in dics and dics[cur.left]:
                cur = cur.left
            else:
                cur = cur.right
            res.append("U")

        cur = mid
        while cur.val != destValue:
            if cur.left in dice and dice[cur.left]:
                cur = cur.left
                res.append("L")
            else:
                cur = cur.right
                res.append("R")

        return "".join(res)