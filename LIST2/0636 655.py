# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def height(cur):
            if not cur:
                return 0
            return 1 + max(height(cur.left), height(cur.right))

        h = height(root)
        w = 2 ** h - 1
        res = [[""] * w for _ in range(h)]

        def ref(l, r, h, cur):
            if not cur:
                return
            mid = (l + r) // 2
            res[h - 1][mid] = str(cur.val)
            ref(l, mid - 1, h + 1, cur.left)
            ref(mid + 1, r, h + 1, cur.right)

        ref(0, w - 1, 1, root)

        return res