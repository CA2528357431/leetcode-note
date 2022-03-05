class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def deal(num):
            if num == 0:
                return mapping[0]
            li = []
            while num:
                li.append(num % 10)
                num = num // 10
            res = 0
            for i in range(len(li) - 1, -1, -1):
                ori = li[i]
                neo = mapping[ori]
                res = res * 10 + neo
            return res

        nums.sort(key=lambda x: deal(x))
        return nums

