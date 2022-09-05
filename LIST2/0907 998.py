# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        while True:
            if cur.val < val:

                num = cur.val
                cur.val = val
                val = num

                neo = TreeNode(val)
                neo.left = cur.left
                neo.right = cur.right

                cur.left = neo
                cur.right = None

                break


            elif not cur.right:
                neo = TreeNode(val)
                cur.right = neo
                break
            else:
                cur = cur.right

        return root