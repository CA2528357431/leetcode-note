class Solution:
    def minimizeResult(self, expression: str) -> str:
        nums = expression.split("+")
        num0 = int(nums[0])
        num1 = int(nums[1])

        li = None
        res = 999999999999

        for i in range(len(nums[0])):
            for j in range(len(nums[1])):
                n00 = nums[0][:i]
                n01 = nums[0][i:]
                n10 = nums[1][:len(nums[1]) - j]
                n11 = nums[1][len(nums[1]) - j:]

                num00 = 1
                if n00:
                    num00 = int(n00)
                num01 = int(n01)
                num10 = int(n10)
                num11 = 1
                if n11:
                    num11 = int(n11)

                neo = num00 * (num01 + num10) * num11

                if neo < res:
                    li = n00 + "(" + n01 + "+" + n10 + ")" + n11
                    res = neo

        return li