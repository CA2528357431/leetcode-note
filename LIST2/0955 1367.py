# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        li = []
        cur = head
        while cur:
            li.append(cur.val)
            cur = cur.next

        n = len(li)

        def getnext(li):

            res = [0] * n

            cur = 1
            length = 0
            while cur < n:
                if li[length] == li[cur]:
                    res[cur] = length + 1
                    cur += 1
                    length += 1
                elif length == 0:
                    cur += 1
                else:
                    length = res[length - 1]

            return res

        nxt = getnext(li)

        def do(treenode, i):
            # print(treenode.val,i)
            if i == n:
                return True
            if not treenode:
                return False
            if li[i] == treenode.val:
                l = do(treenode.left, i + 1)
                r = do(treenode.right, i + 1)
                if l or r:
                    return True
                else:
                    return False
            else:
                if i == 0:
                    l = do(treenode.left, 0)
                    r = do(treenode.right, 0)
                    if l or r:
                        return True
                    else:
                        return False
                else:
                    return do(treenode, nxt[i - 1])

        return do(root, 0)