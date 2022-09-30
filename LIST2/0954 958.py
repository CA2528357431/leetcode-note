# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        cur = [root]
        full = True

        while cur:
            nxt = []
            stop = False
            for x in cur:
                if stop == True:
                    if x.left or x.right:
                        return False

                if x.left and x.right:
                    nxt.append(x.left)
                    nxt.append(x.right)
                elif x.left:
                    stop = True
                    nxt.append(x.left)
                elif x.right:
                    return False
                else:
                    stop = True

            if not full:
                if len(nxt) != 0:
                    return False
                else:
                    return True
            else:
                if stop:
                    full = False
                    cur = nxt
                else:
                    cur = nxt

        return True
