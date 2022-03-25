class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        def deal(string):
            cnt = 0
            for c in string:
                cnt = cnt*2+int(c)
            return cnt
        def get(num):
            li = [""]*n
            for i in range(n):
                li[n-i-1] = str(num%2)
                num = num//2
            return "".join(li)
        dealnums = [deal(x) for x in nums]
        dealnums.sort()
        if dealnums[0]>0:
            return "0"*n
        for i in range(n-1):
            if dealnums[i+1]-dealnums[i]>1:
                return get(dealnums[i]+1)
        return get(dealnums[-1]+1)
