class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        big = 3**19
        if n<=0:
            return False

        if big%n:
            return False
        else:
            return True