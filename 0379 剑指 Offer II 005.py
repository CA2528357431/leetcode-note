class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        li = [0] * n

        dic = [0] * 26

        for ind in range(n):

            word = words[ind]
            cur = dic.copy()
            for c in word:
                i = ord(c) - ord("a")
                cur[i] = 1

            bit = 0

            mul = 1
            for num in cur:
                bit += mul * num
                mul *= 2

            li[ind] = bit

        res = 0
        for i in range(n):

            for j in range(i + 1, n):
                if li[i] & li[j] == 0:
                    res = max(len(words[i]) * len(words[j]), res)
        return res

    # 当数据的元素有确定范围时，考虑位运算
