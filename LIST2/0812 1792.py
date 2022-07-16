class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        stack = []
        heapq.heapify(stack)
        for p,t in classes:
            heapq.heappush(stack, (((p / t) - 1) / (t + 1), p, t))
        for i in range(extraStudents):
            delta, a, b = heapq.heappop(stack)
            if 1 - delta <= 10 ** (-6):
                return 1.0
            a += 1
            b += 1
            heapq.heappush(stack, (((a / b) - 1) / (b + 1), a, b))

        ans = 0

        for _,p,t in stack:
            ans += p/t

        return ans / len(stack)
    # 没事别自己创建类