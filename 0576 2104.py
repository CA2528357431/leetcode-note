class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        # 单调栈
        # https://leetcode-cn.com/problems/sum-of-subarray-ranges/solution/zi-shu-zu-fan-wei-he-by-leetcode-solutio-lamr/

        n = len(nums)
        leftstackmin = []
        leftindexmin = [0] * n
        leftstackmax = []
        leftindexmax = [0] * n
        for i in range(n):
            num = nums[i]
            while leftstackmin and nums[leftstackmin[-1]] > num:
                leftstackmin.pop()
            if not leftstackmin:
                leftindexmin[i] = -1
            else:
                leftindexmin[i] = leftstackmin[-1]
            leftstackmin.append(i)

            while leftstackmax and nums[leftstackmax[-1]] < num:
                leftstackmax.pop()
            if not leftstackmax:
                leftindexmax[i] = -1
            else:
                leftindexmax[i] = leftstackmax[-1]
            leftstackmax.append(i)

        rightstackmin = []
        rightindexmin = [0] * n
        rightstackmax = []
        rightindexmax = [0] * n
        for i in range(n - 1, -1, -1):
            num = nums[i]

            while rightstackmin and nums[rightstackmin[-1]] >= num:
                rightstackmin.pop()
            if not rightstackmin:
                rightindexmin[i] = n
            else:
                rightindexmin[i] = rightstackmin[-1]
            rightstackmin.append(i)

            while rightstackmax and nums[rightstackmax[-1]] <= num:
                rightstackmax.pop()
            if not rightstackmax:
                rightindexmax[i] = n
            else:
                rightindexmax[i] = rightstackmax[-1]
            rightstackmax.append(i)

        res = 0
        for i in range(n):
            p = (rightindexmax[i] - i) * (i - leftindexmax[i])
            n = (rightindexmin[i] - i) * (i - leftindexmin[i])

            res = res + (p - n) * nums[i]
        return res