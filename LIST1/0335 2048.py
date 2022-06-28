class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def judge(x):
            li = str(x)
            dic = {}
            for c in li:
                dic[c] = dic.get(c, 0) + 1
            for k, v in dic.items():
                if k != str(v):
                    return False
            return True

        x = n + 1
        while True:
            if judge(x):
                return x
            else:
                x += 1
