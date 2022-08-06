# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            neo = TreeNode(val)
            neo.left = root
            return neo
        cur = [root]
        for i in range(depth - 2):
            neo = []
            for n in cur:
                if n.left:
                    neo.append(n.left)
                if n.right:
                    neo.append(n.right)
            cur = neo

        nxt = []
        for n in cur:
            neol = TreeNode(val)
            neol.left = n.left
            n.left = neol
            neor = TreeNode(val)
            neor.right = n.right
            n.right = neor
        return root
