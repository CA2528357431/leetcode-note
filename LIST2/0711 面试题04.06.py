# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:

        def find(c):
            if not c:
                return None

            if c.val > p.val:
                l = find(c.left)
                if not l:
                    return c
                else:
                    return l
            else:
                return find(c.right)

        return find(root)