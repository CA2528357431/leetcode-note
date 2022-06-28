# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(inorder)
        indic = {inorder[i]: i for i in range(n)}

        def deal(prel, prer, inl, inr):
            if inl > inr or prel > prer:
                return None

            val = preorder[prel]
            root = TreeNode(val)

            mid = indic[val]
            llen = (mid - 1) - (inl) + 1
            rlen = inr - (mid + 1) + 1

            root.left = deal(prel + 1, prel + llen, inl, mid - 1)
            root.right = deal(prer - rlen + 1, prer, mid + 1, inr)
            return root

        return deal(0, n - 1, 0, n - 1)