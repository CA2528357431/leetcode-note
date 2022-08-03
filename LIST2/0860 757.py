class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        # 实际上遍历的，是射击位置
        # 从左向右遍历时，射击位置在气球右侧
        # 因此第一个key是x[1]

        # 第二个key是子集问题，如果start大的气球能满足，则同end且start小的气球也满足

        res = 0
        times = 2
        n = len(intervals)

        vals = [0 for _ in range(n)]

        for i in range(n):
            cur = intervals[i][1]
            for _ in range(times - vals[i]):
                res += 1
                for j in range(i + 1, n):
                    if intervals[j][0] > cur:
                        break
                    vals[j] += 1
                cur -= 1
        return res