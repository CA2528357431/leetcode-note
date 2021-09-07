class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cur = None
        stack = 0
        num = 0
        for i in range(len(s)):
            if stack==0:
                cur = s[i]
                stack+=1
                num+=1
                continue
            if s[i]==cur:
                stack+=1
            else:
                stack-=1
        return num