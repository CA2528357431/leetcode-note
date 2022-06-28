# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def mid(cur):
            if not cur:
                return[]
            return mid(cur.left)+[cur.val]+mid(cur.right)
        li = mid(root)
        return li[k-1]