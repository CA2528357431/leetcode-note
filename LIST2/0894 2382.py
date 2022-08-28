from sortedcontainers import SortedDict


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:

        n = len(nums)

        sli = nums.copy()
        for i in range(1, n):
            sli[i] += sli[i - 1]

        s = sum(nums)

        li = SortedDict()
        val = {}
        li[0] = n - 1
        val[0] = s

        res = []

        sset = SortedDict()
        sset[s] = 1

        def do(i):
            left = 0
            right = len(li) - 1
            ks = li.keys()
            while left < right:
                mid = (left + right) // 2 + 1
                if ks[mid] <= i:
                    left = mid
                elif ks[mid] > i:
                    right = mid - 1

            l = ks[left]
            if li[l] == l:
                sset[val[l]] -= 1
                if sset[val[l]] == 0:
                    sset.pop(val[l])
                li.pop(l)
                val.pop(l)
            elif i == l:
                ss = val[l] - nums[i]
                ii = li[l]
                sset[val[l]] -= 1
                if sset[val[l]] == 0:
                    sset.pop(val[l])
                li.pop(l)
                val.pop(l)
                li[l + 1] = ii
                val[l + 1] = ss
                if ss not in sset:
                    sset[ss] = 0
                sset[ss] += 1
            elif i == li[l]:
                sset[val[l]] -= 1
                if sset[val[l]] == 0:
                    sset.pop(val[l])
                li[l] -= 1
                val[l] -= nums[i]
                if val[l] not in sset:
                    sset[val[l]] = 0
                sset[val[l]] += 1


            else:
                ls = l
                rs = i + 1
                le = i - 1
                re = li[l]
                lsum = sli[le]
                if ls > 0:
                    lsum -= sli[ls - 1]
                rsum = sli[re]
                if rs > 0:
                    rsum -= sli[rs - 1]

                sset[val[l]] -= 1
                if sset[val[l]] == 0:
                    sset.pop(val[l])
                li.pop(l)
                val.pop(l)
                li[ls] = le
                li[rs] = re
                val[ls] = lsum
                val[rs] = rsum
                if lsum not in sset:
                    sset[lsum] = 0
                sset[lsum] += 1
                if rsum not in sset:
                    sset[rsum] = 0
                sset[rsum] += 1

            if sset:
                res.append(sset.keys()[-1])
            else:
                res.append(0)

        for i in removeQueries:
            do(i)
        return res