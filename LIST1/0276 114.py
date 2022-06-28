# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 遍历
        '''
        re = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                re.append(cur)
                cur = cur.left
            if stack:
                cur = stack.pop().right
        for i in range(len(re) - 1):
            re[i].left = None
            re[i].right = re[i + 1]
        '''


        # 原地操作

        # https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/
        if not root:
            return

        cur = root
        while cur:
            if cur.left:
                r = cur.right
                l = cur.left
                while l.right:
                    l = l.right
                l.right = r
                cur.left, cur.right = None, cur.left
            cur = cur.right