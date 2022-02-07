class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        def geteach(num):
            num = abs(num)
            res = []
            while num:
                res.append(num % 10)
                num = num // 10
            return res

        li = geteach(num)
        pn = 1
        if num < 0:
            li.sort(reverse=True)
            pn = -1
        else:
            li.sort()
        if li[0] == 0:
            for i in range(len(li)):
                if li[i] != 0:
                    li[0] = li[i]
                    li[i] = 0
                    break

        def getnum(li):
            cur = 0
            for num in li:
                cur = cur * 10 + num
            return cur

        return pn * getnum(li)