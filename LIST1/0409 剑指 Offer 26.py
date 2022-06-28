# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return False

        def same(cur, target):
            if (not cur and not target) or (cur and not target):
                return True
            elif not cur and target:
                return False
            else:
                if cur.val != target.val:
                    return False
                l = same(cur.left, target.left)
                r = same(cur.right, target.right)
                return l and r

        def judge(cur, target):
            if not cur:
                return False

            if cur.val == target.val:
                now = same(cur, target)
                if now:
                    return True

            l = judge(cur.left, target)
            r = judge(cur.right, target)
            return l or r

        return judge(A, B)