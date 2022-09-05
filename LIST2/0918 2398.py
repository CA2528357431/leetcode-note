class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:

        n = len(chargeTimes)

        cur = deque()

        res = 0

        cnt = 0
        s = 0
        j = 0
        for i in range(n):
            while cur and cur[-1] < chargeTimes[i]:
                cur.pop()
            cur.append(chargeTimes[i])
            s += runningCosts[i]
            cnt += 1

            while j <= i and s * cnt + cur[0] > budget:
                cnt -= 1
                s -= runningCosts[j]

                if chargeTimes[j] == cur[0]:
                    cur.popleft()
                j += 1

            res = max(cnt, res)
        return res
        # 参考239