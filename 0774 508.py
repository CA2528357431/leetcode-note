# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        dic = {}
        res = []
        num = 0

        def do(cur):
            nonlocal num, res
            if not cur:
                return 0

            l = do(cur.left)
            r = do(cur.right)
            m = l + r + cur.val

            if m not in dic:
                dic[m] = 0
            dic[m] += 1

            if dic[m] > num:
                res = [m]
                num = dic[m]
            elif dic[m] == num:
                res.append(m)
            return m

        do(root)
        return res