class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = [1] * (n + 1)
        for i in range(1, n + 1):
            num[i] = num[i - 1] * (i)
        used = [False] * n
        res = ""
        k -= 1


        def do(cur):
            if cur == 0:
                return

            nonlocal k
            nonlocal res

            neonum = k // num[cur - 1]+1

            i = 0
            for ii in range(n):
                if not used[ii]:
                    i+=1
                    if i==neonum:
                        used[ii] = True
                        res += str(ii + 1)
                        break
            k = k % num[cur - 1]


            do(cur - 1)

        do(n)
        return res