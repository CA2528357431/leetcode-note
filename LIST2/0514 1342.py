class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            ans += num & 1
            if num > 1:
                ans += 1
            num >>= 1
        return ans