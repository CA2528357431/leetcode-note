from sortedcontainers import SortedDict


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        numsDivide = list(set(numsDivide))
        numsDivide.sort()

        dic = SortedDict()
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1

        res = 0
        ks = list(dic.keys())
        for k in ks:
            if k > numsDivide[0]:
                break
            j = True
            for x in numsDivide:
                if x % k != 0:
                    j = False
                    break
            if j:
                return res
            else:
                res += dic[k]

        return -1
