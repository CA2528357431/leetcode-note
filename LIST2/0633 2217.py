class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        nl = (intLength + 1) // 2
        froml = 10 ** (nl - 1)
        tol = 10 ** nl - 1

        def get(froml, tol, i):
            num = tol - froml + 1
            if i > num:
                return -1
            return froml - 1 + i

        re = [get(froml, tol, i) for i in queries]

        def add(x):
            if x == -1:
                return -1
            if intLength % 2 == 0:
                string = str(x) + str(x)[::-1]
                return int(string)
            else:
                string = str(x) + str(x)[::-1][1:]
                return int(string)

        res = [add(i) for i in re]

        return res