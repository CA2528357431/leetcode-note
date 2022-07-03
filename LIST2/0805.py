# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        if n == 1:
            mat = [[-1] for _ in range(m)]
            cur = head
            i = 0
            while cur:
                mat[i][0] = cur.val
                cur = cur.next
                i += 1
            return mat

        mat = [[-1] * n for _ in range(m)]
        i = 0
        j = 0

        typ = [[0, n - 1], [m - 1, n - 1], [m - 1, 0], [1, 0]]
        st = 0
        mov = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        cur = head
        while cur:
            mat[i][j] = cur.val
            cur = cur.next
            i += mov[st][0]
            j += mov[st][1]
            if i == typ[st][0] and j == typ[st][1]:
                if st == 0:
                    typ[st][0] += 1
                    typ[st][1] -= 1
                elif st == 1:
                    typ[st][0] -= 1
                    typ[st][1] -= 1
                elif st == 2:
                    typ[st][0] -= 1
                    typ[st][1] += 1
                else:
                    typ[st][0] += 1
                    typ[st][1] += 1

                st = (st + 1) % 4
        return mat
