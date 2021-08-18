class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        old = x
        neo = 0
        while x!=0:
            t = x%10
            neo = 10*neo+t
            x = x//10
        return neo==old