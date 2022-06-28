# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        neo = TreeNode(val)
        if not root:
            return neo

        cur = root
        while cur:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = neo
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = neo
                    break
        return root