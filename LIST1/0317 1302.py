# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        queue = [root]
        while queue:
            neo = []
            for x in queue:
                if x.left:
                    neo.append(x.left)
                if x.right:
                    neo.append(x.right)

            if not neo:
                return sum(x.val for x in queue)
            else:
                queue = neo