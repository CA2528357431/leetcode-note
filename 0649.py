class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        candies.sort()
        n = len(candies)
        l = 1
        r = candies[-1]

        while l < r:
            j = (l + r) // 2 + 1
            sc = 0
            for i in range(n):
                sc += candies[i] // j

            if sc >= k:
                l = j
            else:
                r = j - 1

        return l