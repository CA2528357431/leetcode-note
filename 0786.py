class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        li = [0] * 30

        def do(i):
            j = 0
            while i:
                li[j] += i % 2
                i //= 2
                j += 1

        for n in nums:
            do(n)
        res = 0
        for i in range(30):
            neo = (2 ** i)
            if li[i] != 0:
                res += neo
        return res
