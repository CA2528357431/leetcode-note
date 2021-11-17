# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        cur = [root]
        while cur:
            neo = []
            for x in cur:
                res.append(x.val)
                if x.left:
                    neo.append(x.left)
                if x.right:
                    neo.append(x.right)
            cur = neo
        return res