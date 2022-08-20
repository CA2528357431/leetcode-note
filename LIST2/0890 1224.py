class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        countnum = {}
        counttime = {}

        res = 1
        big = 0
        s = set()

        for i in range(len(nums)):
            num = nums[i]
            countnum[num] = countnum.get(num, 0) + 1
            counttime[countnum[num]] = counttime.get(countnum[num], 0) + 1

            if countnum[num] > 1:
                counttime[countnum[num] - 1] -= 1

            big = max(countnum[num], big)
            s.add(num)

            if big > 1 and counttime[big] == 1 and counttime[big - 1] == len(s) - 1:
                res = max(res, i + 1)
            elif big > 1 and counttime[big] == len(s) - 1 and counttime[1] == 1:
                res = max(res, i + 1)
            elif big == 1 and counttime[big] == len(s):
                res = max(res, i + 1)
        return res