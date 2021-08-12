# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        '''
        def mid(root):
            if not root:
                return []
            return mid(root.left)+[root.val]+mid(root.right)
        li = mid(root)
        l = 0
        r = len(li)-1
        while l<r:
            if li[l]+li[r]>k:
                r-=1
            elif li[l]+li[r]<k:
                l+=1
            else:
                return True
        return False
        '''

        used = set()
        queue = [root]

        while queue:
            cur = queue.pop()
            if k - cur.val in used:
                return True

            else:
                used.add(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return False