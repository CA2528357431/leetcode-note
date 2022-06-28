# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        # 递归

        '''
        def check(left,right):
            if not left and not right:
                return True
            elif left and right:
                return left.val==right.val and check(left.left,right.right) and check (left.right,right.left)
            else:
                return False
        return check(root.left,root.right)
        '''

        # 非递归

        lstack = []
        rstack = []
        l = root.left
        r = root.right
        while (l and r) or (lstack and rstack):
            if l and r:
                if l.val == r.val:
                    lstack.append(l)
                    rstack.append(r)
                    l = l.left
                    r = r.right
                else:
                    return False
            elif not l and not r:
                l = lstack.pop().right
                r = rstack.pop().left

            else:
                return False
        if l != r:
            return False
        else:
            return True