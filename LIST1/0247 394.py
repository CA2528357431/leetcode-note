class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        chs = []
        num = 0
        for c in s:
            if c.isnumeric():
                num = num * 10 + int(c)
            else:
                if num:
                    nums.append(num)
                    num = 0
                if c == "[":
                    chs.append(c)
                elif c == "]":
                    ch = ""
                    while True:
                        cc = chs.pop()
                        if cc == "[":
                            break
                        ch = cc + ch
                    n = nums.pop()
                    chs.append(ch * n)
                else:
                    chs.append(c)
        return "".join(chs)



