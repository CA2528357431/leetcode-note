class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        li = [i for i in range(n) if s[i] == c]
        li.append(9999999)
        li.insert(0, -9999999)
        cur = 0
        res = [0] * n
        for i in range(n):
            res[i] = min(i - li[cur], li[cur + 1] - i)

            if i == li[cur + 1]:
                cur += 1
        return res