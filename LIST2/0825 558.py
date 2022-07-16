"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':

        if not quadTree1 or not quadTree2:
            return None

        def do(a, b):

            if a.isLeaf:
                if a.val:
                    neo = Node(True, True, None, None, None, None)
                    return neo
                else:
                    return b

            if b.isLeaf:
                if b.val:
                    neo = Node(True, True, None, None, None, None)
                    return neo
                else:
                    return a

            n1 = do(a.topLeft, b.topLeft)
            n2 = do(a.topRight, b.topRight)
            n3 = do(a.bottomLeft, b.bottomLeft)
            n4 = do(a.bottomRight, b.bottomRight)

            if n1.isLeaf and n2.isLeaf and n3.isLeaf and n4.isLeaf and n1.val == n2.val == n3.val == n4.val:
                return n1
            neo = Node(a.val | b.val, False, n1, n2, n3, n4)
            return neo

        res = do(quadTree1, quadTree2)
        return res