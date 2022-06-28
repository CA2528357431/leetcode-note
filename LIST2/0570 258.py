class Solution:
    def addDigits(self, num: int) -> int:
        def do(num):
            if num<10:
                return num
            neo=0
            while num:
                neo+=num%10
                num=num//10
            return do(neo)
        return do(num)