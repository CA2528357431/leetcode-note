class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        lower = 10 ** (n-1)
        for l in range(upper, lower-1, -1):
            num = int(str(l)+str(l)[::-1])
            x = upper
            while x * x >= num:
                if num % x == 0:
                    return num % 1337
                x -= 1