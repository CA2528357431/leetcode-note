class Solution:
    def longestPalindrome(self, s):

        # 注意，起始状态有奇回文和偶回文

        '''
        res = [[False] * len(s) for _ in range(len(s))]
        for x in range(len(s) - 1):
            res[x][x] = True
            if s[x] == s[x + 1]:
                res[x][x + 1] = True
        res[-1][-1] = True

        for r in range(2, len(s)):
            for x in range(0, len(s) - r):
                if s[x] == s[x + r] and res[x + 1][x + r - 1]:
                    res[x][x + r] = True

        for r in range(len(s))[::-1]:
            for x in range(0, len(s) - r):
                if res[x][x + r]:
                    return s[x:x + r + 1]
        '''


        # 双指针

        start, end = 0, 0
        for x in range(len(s)):
            l = r = x
            while l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            if r - l + 1 > end - start + 1:
                start, end = l, r
        for x in range(len(s) - 1):
            l = x
            r = x + 1
            if s[l] == s[r]:
                while l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
                    l -= 1
                    r += 1
                if r - l + 1 > end - start + 1:
                    start, end = l, r
        return s[start:end + 1]

