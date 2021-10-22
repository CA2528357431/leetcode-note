class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnum = 0
        rnum = 0
        onum = 0
        anum = 0
        # 保存各个状态的个数

        num = 0
        for c in croakOfFrogs:
            if c == "c":
                cnum += 1

            elif c == "r":
                if cnum == 0:
                    return -1
                else:
                    cnum -= 1
                    rnum += 1

            elif c == "o":
                if rnum == 0:
                    return -1
                else:
                    rnum -= 1
                    onum += 1

            elif c == "a":
                if onum == 0:
                    return -1
                else:
                    onum -= 1
                    anum += 1

            elif c == "k":
                if anum == 0:
                    return -1
                else:
                    num = max(num, cnum + rnum + onum + anum)
                    anum -= 1

            # 更新状态


            else:
                return -1

        if cnum or rnum or onum or anum:
            return -1
        else:
            return num