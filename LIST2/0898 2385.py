# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if start == root.val:
            cur = [root]
            res = 0
            while cur:
                nxt = []
                for x in cur:
                    if x.left:
                        nxt.append(x.left)
                    if x.right:
                        nxt.append(x.right)
                cur = nxt

                res += 1
            return res - 1

        cur = [root]
        neo = []
        while cur:
            nxt = []
            for x in cur:
                if x.val == start:
                    neo.append(x)
                    continue
                if x.left:
                    nxt.append(x.left)
                if x.right:
                    nxt.append(x.right)
            cur = nxt
            if neo:
                break

        after = 0
        while neo:
            nxt = []
            for x in neo:
                if x.left:
                    nxt.append(x.left)
                if x.right:
                    nxt.append(x.right)
            neo = nxt

            after += 1

        dichave = {}

        def have(cur):
            if not cur:
                return -1
            if cur.val == start:
                return 0
            if cur in dichave:
                return dichave[cur]
            l = have(cur.left)
            r = have(cur.right)
            if l == -1 and r == -1:
                dichave[cur] = -1
                return -1
            else:
                dichave[cur] = max(l, r) + 1
                return dichave[cur]

        dicheight = {}

        def height(cur):
            if not cur:
                return 0
            if cur in dicheight:
                return dicheight[cur]
            l = height(cur.left)
            r = height(cur.right)
            dicheight[cur] = max(l, r) + 1
            return dicheight[cur]

        height(root)
        have(root)
        dis = 0
        cur = root
        while cur.val != start:
            if have(cur.left) >= 0:
                a = cur.left
                b = cur.right
            else:
                b = cur.left
                a = cur.right
            hf = have(a)
            he = height(b)
            dis = max(he + hf + 1, dis)
            cur = a
        # print(dis,after)

        return max(dis, after - 1)