class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dic0 = {}
        dic1 = {}

        for i in range(len(nums)):
            num = nums[i]
            if i % 2 == 0:
                dic0[num] = dic0.get(num, 0) + 1
            else:
                dic1[num] = dic1.get(num, 0) + 1

        li0 = list(dic0.keys())
        li0.sort(key=lambda x: -dic0[x])
        li1 = list(dic1.keys())
        li1.sort(key=lambda x: -dic1[x])

        n0 = len(li0)
        n1 = len(li1)

        res = 99999



        # 令奇数最佳或者偶数最佳即可
        x = -1
        y = -1
        i1 = 0
        while i1 < n1:
            if i1 > 0 and dic1[li1[i1]] != dic1[li1[i1 - 1]]:
                break
            x = li1[i1]
            i0 = 0
            while i0 < n0:
                if li0[i0] != x:
                    y = li0[i0]
                    break
                i0 += 1

            if y == -1:
                neo = len(nums) - dic1[x]
                res = min(neo, res)
            else:
                neo = len(nums) - dic1[x] - dic0[y]
                res = min(neo, res)
            i1 += 1
        x = -1
        y = -1
        i0 = 0
        while i0 < n0:
            if i0 > 0 and dic0[li0[i0]] != dic0[li0[i0 - 1]]:
                break
            x = li0[i0]
            i1 = 0
            while i1 < n1:
                if li1[i1] != x:
                    y = li1[i1]
                    break
                i1 += 1

            if y == -1:
                neo = len(nums) - dic0[x]
                res = min(neo, res)
            else:
                neo = len(nums) - dic0[x] - dic1[y]
                res = min(neo, res)
            i0 += 1
        return res