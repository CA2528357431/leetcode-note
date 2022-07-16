# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def do(cur):
            if not cur.left or not cur.right:
                if cur.val==1:
                    return True
                else:
                    return False
            l = do(cur.left)
            r = do(cur.right)
            if cur.val==2:
                return l or r
            else:
                return l and r
        return do(root)