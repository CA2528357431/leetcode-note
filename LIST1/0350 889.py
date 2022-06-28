# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(preorder)
        predic = {preorder[i]: i for i in range(n)}

        def create(prel, prer, postl, postr):
            if prel > prer:
                return None

            root = TreeNode(preorder[prel])
            if prel == prer:
                return root

            rnum = postorder[postr - 1]
            index = predic[rnum]
            rlen = prer - index + 1

            root.right = create(index, prer, postr - rlen, postr - 1)
            root.left = create(prel + 1, index - 1, postl, postr - rlen - 1)

            return root

        return create(0, n - 1, 0, n - 1)