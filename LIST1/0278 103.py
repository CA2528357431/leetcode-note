# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        i = 0
        res = [[root.val]]
        cur = [root]
        while cur:

            neo = []
            for x in cur:
                if x.left:
                    neo.append(x.left)
                if x.right:
                    neo.append(x.right)
            if not neo:
                break
            cur = neo
            nums = [x.val for x in neo]
            i += 1
            if i % 2 == 1:
                res.append(nums[::-1])
            else:
                res.append(nums)

        return res