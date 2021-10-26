# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def dfs(l, r):
            if l > r:
                return [None]
            trees = []
            for i in range(l, r + 1):

                lnodes = dfs(l, i - 1)
                rnodes = dfs(i + 1, r)
                for lnode in lnodes:
                    for rnode in rnodes:
                        root = TreeNode(i)
                        root.left = lnode
                        root.right = rnode
                        trees.append(root)
            return trees