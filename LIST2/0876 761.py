class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def do(s):
            if len(s) <= 2:
                return s

            cur = 0
            start = 0
            li = list()

            for i in range(len(s)):
                ch = s[i]
                if ch == "1":
                    cur += 1
                else:
                    cur -= 1
                    if cur == 0:
                        neo = "1" + do(s[start + 1:i]) + "0"
                        li.append(neo)
                        start = i + 1
            # s[start+1:i] 必然是1开头0结尾
            # 如果0开头，则s[start]、start[start+1]构成10序列，直接截断
            li.sort(reverse=True)
            return "".join(li)

        return do(s)