class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s = sum(nums)
        tar = s / 2

        li = [-x for x in nums]
        heapq.heapify(li)

        i = 0
        while s > tar:
            i += 1
            neo = -heapq.heappop(li)
            s -= neo / 2
            heapq.heappush(li, -neo / 2)

        return i