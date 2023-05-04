class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)

        a1 = 0
        a2 = 0

        for i in range(n):
            r = i
            l = max(0, i - 2)

            if 10 in player1[l:r]:
                a1 += player1[i] * 2
            else:
                a1 += player1[i]

            if 10 in player2[l:r]:
                a2 += player2[i] * 2
            else:
                a2 += player2[i]

        if a1 > a2:
            return 1
        elif a1 < a2:
            return 2
        else:
            return 0

