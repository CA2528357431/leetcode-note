# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        '''
        def decode(cur):
            if not cur:
                return "."
            return str(cur.val) + "," + decode(cur.left) + "," + decode(cur.right)

        res = []
        used = {}

        def do(cur):
            if not cur:
                return
            string = decode(cur)
            if string not in used:
                used[string] = 0
            used[string] += 1
            if used[string] == 2:
                res.append(cur)
            do(cur.left)
            do(cur.right)

        do(root)

        return res
        '''

        # 在递归的途中就进行处理
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