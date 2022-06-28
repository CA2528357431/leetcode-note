# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True


        # 左子树的max必须小于根
        left = True
        if root.left:
            cur = root.left
            while cur and cur.right:
                cur = cur.right
            left = cur.val < root.val

        right = True
        if root.right:
            cur = root.right
            while cur and cur.left:
                cur = cur.left
            right = cur.val > root.val

        mid = True
        if root.left:
            mid = mid and root.left.val < root.val
        if root.right:
            mid = mid and root.val < root.right.val

        return mid and right and left and self.isValidBST(root.left) and self.isValidBST(root.right)