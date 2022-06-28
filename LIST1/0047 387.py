class Solution:
    def firstUniqChar(self, s: str) -> int:

        '''
        a = set()
        b = set()
        for x in s:
            if x in a:
                b.add(x)
            if x not in a:
                a.add(x)
        for x in range(len(s)):
            if s[x] in a and s[x] not in b:
                return x
        return -1
        '''

        a = {}
        for x in range(len(s)):
            if s[x] in a:
                a[s[x]] = -1
            else:
                a[s[x]] = x
        for x in range(len(s)):
            if a[s[x]] != -1:
                return a[s[x]]
        return -1

        # 考虑好 key value