# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dic = {}

        def do(x):

            if x == 1:
                return [TreeNode()]
            if x in dic:
                return dic[x]
            res = []
            for i in range(1, x):
                ls = do(i)
                rs = do(x - 1 - i)
                for l in ls:
                    for r in rs:
                        neo = TreeNode()
                        neo.left = l
                        neo.right = r
                        res.append(neo)
            dic[x] = res
            return res

        return do(n)
