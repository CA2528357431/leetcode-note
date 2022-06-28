# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic = {}
        child = set()
        parent = set()
        for r,c,j in descriptions:
            if r not in dic:
                dic[r] = TreeNode(r)
            if c not in dic:
                dic[c] = TreeNode(c)
            if j==1:
                dic[r].left = dic[c]
            else:
                dic[r].right = dic[c]
            child.add(c)
            parent.add(r)
        rootindex = list(parent-child)[0]
        return dic[rootindex]