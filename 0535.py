class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        i = 0
        while num1 and num2:
            if num1>=num2:
                num1=num1-num2
            else:
                num2 = num2-num1
            i+=1
        return i