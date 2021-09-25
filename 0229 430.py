"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        stack = []
        cur = head
        while cur or stack:

            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None
            else:
                if cur.next:
                    cur = cur.next

                else:
                    if stack:
                        ne = stack.pop()
                        cur.next = ne
                        ne.prev = cur
                        cur = ne
                    else:
                        break

        return head