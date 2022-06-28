# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        judge = True
        def height(cur):
            if not cur:
                return 0
            else:
                nonlocal judge
                l = height(cur.left)
                r = height(cur.right)
                if abs(l-r)>1:
                    judge = False
                    return 0
                return max(l,r)+1
        height(root)
        return judge

        # 递归的同时更新数据