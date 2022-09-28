class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums) + 2
        neo = 0

        for x in nums:
            neo = neo ^ x
        for x in range(1, n + 1):
            neo = neo ^ x

        mark = neo ^ ((neo - 1) & neo)
        x1 = 0
        x2 = 0

        # print(mark)
        for x in nums:
            if x & mark == mark:

                x1 = x1 ^ x
            else:
                x2 = x2 ^ x

        for x in range(1, n + 1):
            if x & mark:
                x1 = x1 ^ x

            else:
                x2 = x2 ^ x

        return [x1, x2]

