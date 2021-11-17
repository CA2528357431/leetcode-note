# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        cur = [root]
        i = 0
        while cur:
            i+=1
            if i%2:
                res.append([x.val for x in cur])
            else:
                res.append([x.val for x in cur][::-1])

            neo = []
            for x in cur:
                if x.left:
                    neo.append(x.left)
                if x.right:
                    neo.append(x.right)
            cur = neo
        return res