# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        dic = {inorder[i]: i for i in range(n)}

        def build(pre_s, pre_e, in_s, in_e):
            if pre_s > pre_e or in_s > in_e:
                return None

            rootval = preorder[pre_s]
            root = TreeNode(rootval)
            index = dic[rootval]
            llen = index - in_s
            rlen = in_e - index
            root.left = build(pre_s + 1, pre_s + llen, in_s, index - 1)
            root.right = build(pre_e - rlen + 1, pre_e, index + 1, in_e)

            return root

        return build(0, n - 1, 0, n - 1)