from sortedcontainers import SortedDict


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))

        def do(n):
            return bin(n & 0xffffffff).count('1')

        dic = SortedDict()
        for x in nums:
            neo = do(x)
            if neo not in dic:
                dic[neo] = 0
            dic[neo] += 1

        ks = list(dic.keys())

        res = 0

        cur = 0
        j = len(ks) - 1
        for x in ks:
            while j >= 0 and ks[j] + x >= k:
                y = ks[j]
                cur += dic[y]
                j -= 1
            res += cur * dic[x]
            # 双指针遍历
            # cur记录1个数都与等于y的数字的个数

        return res