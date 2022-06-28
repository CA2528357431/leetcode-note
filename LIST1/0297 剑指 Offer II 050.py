# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        '''
        if not root:
            return 0

        def find(cur, tar):
            if not cur:
                return 0

            left = find(cur.left, tar - cur.val)
            right = find(cur.right, tar - cur.val)

            t = left + right

            if tar == cur.val:
                return t + 1
            else:
                return t

        mid = find(root, targetSum)
        l = self.pathSum(root.left, targetSum)
        r = self.pathSum(root.right, targetSum)
        return mid + l + r
        '''


        prefix = {}
        def dfs(cur, num):
            if not cur:
                return 0

            prefix[num] = prefix.get(num, 0) + 1

            num += cur.val

            delta = num - targetSum

            m = prefix.get(delta, 0)

            l = dfs(cur.left, num)
            r = dfs(cur.right, num)

            prefix[num - cur.val] -= 1

            return m + l + r

        t = dfs(root, 0)
        return t