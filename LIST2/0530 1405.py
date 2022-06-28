class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        li = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            li.sort(key=lambda x: -x[0])

            judge = False

            for i in range(3):
                num,ch = li[i]

                if num <= 0:
                    return ''.join(res)

                if len(res) >= 2 and res[-2] == ch and res[-1] == ch:
                    continue

                judge = True
                res.append(ch)
                li[i][0] -= 1
                break
            if not judge:
                return ''.join(res)