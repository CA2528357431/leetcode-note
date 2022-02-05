class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        left = [0] * (n + 1)
        right = [0] * (n + 1)

        lheap = [-x for x in nums[:n]]
        heapq.heapify(lheap)
        lcur = -sum(lheap)
        left[0] = lcur
        for i in range(n):
            idx = n + i
            top = -lheap[0]
            neo = nums[idx]
            if top > neo:
                lcur = lcur - top + neo
                heapq.heappop(lheap)
                heapq.heappush(lheap, -neo)
            left[i + 1] = lcur

        rheap = [x for x in nums[2 * n:]]
        heapq.heapify(rheap)
        rcur = sum(rheap)
        right[0] = rcur
        for i in range(n):
            idx = 2 * n - 1 - i
            top = rheap[0]
            neo = nums[idx]
            if top < neo:
                rcur = rcur - top + neo
                heapq.heappop(rheap)
                heapq.heappush(rheap, neo)
            right[i + 1] = rcur
        for i in range(n + 1):
            left[i] = left[i] - right[n - i]
        return min(left)