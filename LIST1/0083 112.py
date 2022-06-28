# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        # BFS

        '''
        if not root:
            return False
        stack = [(root,root.val)]
        while stack:
            cur,num = stack.pop()
            if cur.left:
                stack.append((cur.left,num+cur.left.val))
            if cur.right:
                stack.append((cur.right,num+cur.right.val))
            if not cur.left and not cur.right:
                if num == targetSum:
                    return True
        return False
        '''


        # 递归
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum==root.val
        left = self.hasPathSum(root.left, targetSum-root.val)
        right = self.hasPathSum(root.right, targetSum-root.val)
        return left or right
