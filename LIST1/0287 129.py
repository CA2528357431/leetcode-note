# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        '''
        if not root:
            return 0
        res = 0
        ns = [root]
        while ns:
            neo = []
            for node in ns:
                if not node.left and not node.right:
                    res += node.val
                else:
                    if node.left:
                        node.left.val += 10 * node.val
                        neo.append(node.left)
                    if node.right:
                        node.right.val += 10 * node.val
                        neo.append(node.right)
            ns = neo

        return res
        '''

        def dfs(cur, num):
            num = num * 10 + cur.val
            if not cur.left and not cur.right:
                return num
            elif cur.left and cur.right:
                return dfs(cur.left, num) + dfs(cur.right, num)
            elif cur.left:
                return dfs(cur.left, num)
            else:
                return dfs(cur.right, num)

        return dfs(root, 0)