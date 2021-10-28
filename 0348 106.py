# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        middic = {inorder[i]: i for i in range(len(inorder))}

        def build(l, r, mid):
            if l > r:
                return None

            midval = postorder[mid]
            root = TreeNode(midval)

            midind = middic[midval]

            llen = midind - l
            rlen = r - midind

            r = build(midind + 1, r, mid - 1)
            l = build(l, midind - 1, mid - 1 - rlen)

            root.left = l
            root.right = r
            return root

        return build(0, len(inorder) - 1, len(postorder) - 1)