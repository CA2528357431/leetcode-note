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
    def construct(self, grid: List[List[int]]) -> 'Node':
        glob = 10

        def do(l, r, u, b):
            nonlocal glob
            if l == r:
                return Node(grid[u][l], True, None, None, None, None)
            else:

                length = (r - l + 1) // 2

                tl = do(l, r - length, u, b - length)
                tr = do(l + length, r, u, b - length)
                bl = do(l, r - length, u + length, b)
                br = do(l + length, r, u + length, b)

                if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
                    return Node(grid[u][l], True, None, None, None, None)
                else:
                    glob += 1
                    return Node(glob, False, tl, tr, bl, br)

        return do(0, len(grid) - 1, 0, len(grid) - 1)