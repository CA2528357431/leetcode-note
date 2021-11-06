# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:

        # 求出每个节点的 最大盗取价值，进行递归
        '''
        dic = {None: 0}

        def deal(node):
            if not node:
                return 0

            # not this
            l = 0
            if node.left in dic:
                l = dic[node.left]
            else:
                l = deal(node.left)

            if node.right in dic:
                r = dic[node.right]
            else:
                r = deal(node.right)

            # this
            m = node.val
            ll, lr, rl, rr = 0, 0, 0, 0

            if node.left:
                if node.left.left in dic:
                    ll = dic[node.left.left]
                else:
                    ll = deal(node.left.left)

                if node.left.right in dic:
                    lr = dic[node.left.right]
                else:
                    lr = deal(node.left.right)

            if node.right:
                if node.right.left in dic:
                    rl = dic[node.right.left]
                else:
                    rl = deal(node.right.left)

                if node.right.right in dic:
                    rr = dic[node.right.right]
                else:
                    rr = deal(node.right.right)

            res = max(l + r, m + ll + lr + rl + rr)
            dic[node] = res

            return res

        return deal(root)
        '''

        # 分别求出每个节点的 ”取本节点的价值“，”不取本节点的价值“
        # 太优雅了
        def deal(root):
            if not root:
                return (0, 0)

            ls, ln = deal(root.left)
            # 取left 和 不取left
            rs, rn = deal(root.right)

            return root.val + ln + rn, max(ls, ln) + max(rs, rn)
            # 前者是”取本节点的价值“，后者是”不取本节点的价值“

        return max(deal(root))