class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:

        res = 0
        cur = 0

        n = 1

        for c in s[::-1]:
            c = int(c)
            cur = cur + c * n
            n = n * 2
            if cur > k:
                break
            if c == 1:
                res += 1
        for c in s:
            if c == "0":
                res += 1
        return res

    # 向全部0中插入1
    # 从后向前插入，保证每次插入的增量递增
