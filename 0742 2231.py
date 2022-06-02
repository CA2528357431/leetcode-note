class Solution:
    def largestInteger(self, num: int) -> int:
        def getli(num):
            lli = list(str(num))
            li = [int(x) for x in lli]
            li.reverse()
            return li

        li = getli(num)
        n = len(li)
        li2 = [x for x in li if x % 2 == 0]
        li1 = [x for x in li if x % 2 == 1]
        sp2 = [i for i in range(n) if li[i] % 2 == 0]
        sp1 = [i for i in range(n) if li[i] % 2 == 1]

        li1.sort()
        li2.sort()

        res = 0

        for i in range(len(li1)):
            res += 10 ** sp1[i] * li1[i]
        for i in range(len(li2)):
            res += 10 ** sp2[i] * li2[i]

        return res
