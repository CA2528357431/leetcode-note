class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:

        n = len(rolls)

        res = 1
        change = [False] * (k + 1)
        cnt = 0

        for i in range(n):
            v = rolls[i]
            if change[v] == False:
                change[v] = True
                cnt += 1
                if cnt == k:
                    cnt = 0
                    res += 1
                    change = [False] * (k + 1)
            # print(cnt)
        return res