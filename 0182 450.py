# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        # 此法更好，但不知为何力扣超时
        '''
        if not root:
            return None
        if root.val != key:
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                root.left = self.deleteNode(root.left, key)
            return root

        if not root.left:
            return root.right
        pre = root
        neo = root.left
        while neo.right:
            pre = neo
            neo = neo.right

        pre.right = neo.left

        neo.left = root.left
        neo.right = root.right

        return neo
        '''
        if not root:
            return None
        if root.val != key:
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                root.left = self.deleteNode(root.left, key)
            return root

        if not root.left:
            return root.right
        neo = root.left
        while neo.right:
            neo = neo.right
        neo.right = root.right

        return root.left


