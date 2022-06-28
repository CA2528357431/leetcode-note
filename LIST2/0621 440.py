class Solution:

    def findKthNumber(self, n: int, k: int) -> int:
        def son(pre):
            cnt = 0
            big = pre
            sml = pre
            while sml <= n:
                big = min(big, n)
                cnt += (big - sml + 1)
                big = big * 10 + 9
                sml = sml * 10
            return cnt

        cur = 1
        k -= 1
        while k > 0:
            sons = son(cur)
            if sons <= k:
                k -= sons
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur


