class Solution:
    def reverseVowels(self, s: str) -> str:
        tar = "aeiouAEIOU"
        li = list(s)
        l = 0
        r = len(s) - 1
        while l <= r:
            if li[l] in tar and li[r] in tar:
                li[l], li[r] = li[r], li[l]
                l += 1
                r -= 1
            elif li[l] in tar:
                r -= 1
            elif li[r] in tar:
                l += 1
            else:
                l += 1
                r -= 1
        res = "".join(li)
        return res



