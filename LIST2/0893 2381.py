class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        string = s
        n = len(s)
        li = [0] * n
        for s, e, d in shifts:
            e += 1
            if d == 1:
                li[s] += 1
                if e < n:
                    li[e] -= 1
            else:
                li[s] -= 1
                if e < n:
                    li[e] += 1
        for i in range(1, n):
            li[i] += li[i - 1]

        def do(x, i):
            num = (ord(x) - ord("a") + i + 26) % 26
            return chr(num + ord("a"))

        res = [""] * n

        for i in range(n):
            res[i] = do(string[i], li[i])
        return "".join(res)
