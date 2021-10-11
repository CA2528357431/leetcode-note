# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        cur = [root]
        res = []
        while cur:
            res.append(cur[-1].val)
            neo = []
            for node in cur:
                if node.left:
                    neo.append(node.left)
                if node.right:
                    neo.append(node.right)
            cur = neo
        return res