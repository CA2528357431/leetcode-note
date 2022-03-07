"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {None: None}
        pre = Node(0)
        cpre = Node(0)
        pre.next = head
        cur = pre
        ccur = cpre
        while cur.next:
            cur = cur.next
            cpy = Node(cur.val)
            ccur.next = cpy
            ccur = ccur.next
            dic[cur] = ccur

        docur = cpre.next
        chcur = head
        while docur:
            docur.random = dic[chcur.random]
            docur = docur.next
            chcur = chcur.next
        return cpre.next