# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        def build(l,r):
            if l>r:
                return None
            elif l==r:
                neo = TreeNode(nums[l])
                return neo
            else:
                mid = (l+r)//2
                neo = TreeNode(nums[mid])
                le = build(l,mid-1)
                ri = build(mid+1,r)
                neo.left = le
                neo.right = ri
                return neo
        return build(0,len(nums)-1)