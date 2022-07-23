# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def do(cur):
            if not cur:
                return None
            l = do(cur.left)
            r = do(cur.right)
            cur.left = l
            cur.right = r

            if not l and not r:
                if cur.val == 1:
                    return cur
                else:
                    return None

            else:
                return cur

        return do(root)