# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # DFS
        '''
        def getNodesNum(cur):
            if not cur:
                return 0
            leftNum = getNodesNum(cur.left)
            rightNum = getNodesNum(cur.right)
            return leftNum + rightNum + 1

        return getNodesNum(root)
        '''
        # BFS
        if not root:
            return 0
        layer = 1
        res = 1
        cur = root
        while cur:
            if cur.right:
                cur = cur.right
                res = res * 2
                layer += 1
            elif cur.left:
                cur = cur.left
                res = res * 2 - 1
                layer += 1
            else:
                break

        if layer == 1:
            return 1
        else:
            print(res)
            res += 2 ** (layer - 1) - 1
            return res