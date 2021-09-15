# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def add(point):
            if not point:
                return []
            return add(point.left) + [point.val] + add(point.right)

        li = add(root)
        li.sort()

        stack = []

        cur = root
        i = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            if stack:
                cur = stack.pop()
                cur.val = li[i]
                i += 1
                cur = cur.right
        return root