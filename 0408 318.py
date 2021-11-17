class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def getindex(c):
            i = ord(c) - ord("a")
            return i

        def getbyte(s):
            li = [0] * 26
            for c in s:
                i = getindex(c)
                li[i] = 1
            res = 0
            mul = 1
            for i in range(26):
                cur = li[i] * mul
                res += cur
                mul = mul * 2
            return res

        li = [getbyte(word) for word in words]

        res = 0
        for i in range(len(words)):
            bytei = li[i]
            for j in range(i + 1, len(words)):
                bytej = li[j]
                if (bytei & bytej) == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

    # 利用位运算进行重复比较