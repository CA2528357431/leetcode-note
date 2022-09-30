# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def judge(a, b):
            if not a and not b:
                return True
            if not (a and b):
                return False

            if a.val != b.val:
                return False

            al = a.left
            ar = a.right
            bl = b.left
            br = b.right

            if (judge(al, bl) and judge(ar, br)) or (judge(al, br) and judge(ar, bl)):
                return True
            else:
                return False

        return judge(root1, root2)

