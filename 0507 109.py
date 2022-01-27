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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def find(start, end):

            f = start
            s = start
            while f != end and f.next != end:
                f = f.next.next
                s = s.next
            return s

        def construct(start, end):
            if start == end:
                return None

            mid = find(start, end)
            root = TreeNode(mid.val)

            l = construct(start, mid)
            r = construct(mid.next, end)

            root.left = l
            root.right = r
            return root

        return construct(head, None)



