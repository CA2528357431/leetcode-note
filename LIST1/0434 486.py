class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        li = [[0] * n for _ in range(n)]

        for i in range(n):
            li[i][i] = nums[i]

        for x in range(n - 2, -1, -1):
            for y in range(x + 1, n):
                li[x][y] = max(nums[x] - li[x + 1][y], nums[y] - li[x][y - 1])
        return li[0][-1] >= 0