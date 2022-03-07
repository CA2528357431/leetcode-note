class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)
        pos = 1

        if num < 0:
            num = -num
            pos = -1
        li = []
        while num:
            li.append(str(num % 7))
            num = num // 7
        if pos == -1:
            li.append("-")
        res = "".join(li[::-1])
        return res