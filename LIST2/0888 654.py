# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def do(l,r):
            if l>r:
                return None
            if l==r:
                return TreeNode(nums[l])
            big = l
            for i in range(l,r+1):
                if nums[i]>nums[big]:
                    big = i
            left = do(l,big-1)
            right = do(big+1,r)
            root = TreeNode(nums[big])
            root.left = left
            root.right = right
            return root
        return do(0,len(nums)-1)