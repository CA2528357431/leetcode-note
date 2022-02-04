class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        maxPos = 0
        maxLen = 0

        def check(typeNum):
            # typeNum为字符串中字符种类

            nonlocal maxPos, maxLen

            lowerCnt = [0] * 26
            upperCnt = [0] * 26

            l = 0
            r = 0

            total = 0
            # 当前字符个数
            cnt = 0
            # 成对字符个数

            while r < len(s):
                idx = ord(s[r].lower()) - ord('a')

                if lowerCnt[idx] + upperCnt[idx] == 0:
                    total += 1
                # 重置total

                if s[r].islower():
                    if lowerCnt[idx] == 0 and upperCnt[idx] > 0:
                        cnt += 1
                    lowerCnt[idx] += 1
                else:
                    if upperCnt[idx] == 0 and lowerCnt[idx] > 0:
                        cnt += 1
                    upperCnt[idx] += 1
                # 重置cnt

                # 调节l
                while total > typeNum:
                    idx = ord(s[l].lower()) - ord('a')

                    if lowerCnt[idx] + upperCnt[idx] == 1:
                        total -= 1
                    # 重置total

                    if s[l].islower():
                        lowerCnt[idx] -= 1
                        if lowerCnt[idx] == 0 and upperCnt[idx] > 0:
                            cnt -= 1
                    else:
                        upperCnt[idx] -= 1
                        if upperCnt[idx] == 0 and lowerCnt[idx] > 0:
                            cnt -= 1
                    # 重置cnt

                    l += 1

                # 调节r
                # 如果新串从、更长就更新结果
                if cnt == typeNum and r - l + 1 > maxLen:
                    maxPos = l
                    maxLen = r - l + 1
                r += 1

        types = len(set(s.lower()))
        for i in range(1, types + 1):
            check(i)
            # i 为字符串中字符种类
        return s[maxPos: maxPos + maxLen]
