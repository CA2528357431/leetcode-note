class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        l = 0
        r = len(ans) - 1
        while True:
            while l < r and not ans[l].isalpha():
                l += 1
            while r > l and not ans[r].isalpha():
                r -= 1
            if l >= r:
                break
            ans[l], ans[r] = ans[r], ans[l]
            l += 1
            r -= 1
        return ''.join(ans)