# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        de = set(to_delete)
        res = []

        def do(cur, start):
            if not cur:
                return None
            if cur.val in de:
                l = cur.left
                r = cur.right
                cur.left = None
                cur.right = None
                do(l, True)
                do(r, True)
                return None
            else:
                l = do(cur.left, False)
                r = do(cur.right, False)
                cur.left = l
                cur.right = r
                if start:
                    res.append(cur)
                return cur

        do(root, True)
        return res
