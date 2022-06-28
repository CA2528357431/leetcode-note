class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s==s[::-1]:
            return 1
        else:
            return 2
        # 本题子序列可以不连续