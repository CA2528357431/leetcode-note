# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        res = []
        used = {}

        def decode(cur):
            if not cur:
                return "."

            l = decode(cur.left)
            r = decode(cur.right)
            string = str(cur.val) + "," + l + "," + r
            if string not in used:
                used[string] = 0
            used[string] += 1
            if used[string] == 2:
                res.append(cur)
            return string

        decode(root)

        return res