class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        '''
        res = []

        def do(p):
            cur = 0
            num = 0

            while p < len(words) and cur <= maxWidth:
                if num == 0:
                    cur += len(words[p])
                    num += 1
                    p += 1
                else:
                    cur += (len(words[p]) + 1)
                    num += 1
                    p += 1

            if cur > maxWidth:
                cur -= (1 + len(words[p - 1]))
                p -= 2
                num -= 1

                if num == 1:
                    neo = words[p] + " " * (maxWidth - cur)
                    res.append(neo)
                else:
                    start = p - num + 1
                    neo = words[start]

                    spa = (maxWidth - cur) // (num - 1)
                    time = (maxWidth - cur) % (num - 1)

                    for i in range(start + 1, start + num):
                        if time > 0:
                            neo += " " * (spa + 2)
                            time -= 1
                        else:
                            neo += " " * (spa + 1)

                        neo += words[i]

                    res.append(neo)

                do(p + 1)

            else:
                start = p - num
                neo = words[start]
                for i in range(start + 1, len(words)):
                    neo += " "
                    neo += words[i]
                neo += " " * (maxWidth - len(neo))
                res.append(neo)
                return

        do(0)
        return res
        '''

        # 不另开函数

        res = []

        # 记录开头结尾的坐标而不是单词本身
        cur = [0, 0]
        num = len(words[0])

        for i in range(1, len(words)):
            if num + len(words[i]) + 1 > maxWidth:
                if cur[0] < cur[1]:
                    spa = (maxWidth - num) // (cur[1] - cur[0])
                    time = (maxWidth - num) % (cur[1] - cur[0])
                    neo = words[cur[0]]
                    for x in range(cur[0] + 1, cur[1] + 1):
                        if time > 0:
                            # 本身一个空格，space的空格，多余的空格
                            neo += " " * (spa + 2)
                            neo += words[x]
                            time -= 1
                        else:
                            neo += " " * (spa + 1)
                            neo += words[x]
                    res.append(neo)
                else:
                    neo = words[cur[0]] + " " * (maxWidth - len(words[cur[0]]))
                    res.append(neo)

                num = len(words[i])
                cur[0], cur[1] = i, i

            else:
                num += len(words[i]) + 1
                cur[1] = i

        neo = words[cur[0]]
        for x in range(cur[0] + 1, cur[1] + 1):
            neo += " "
            neo += words[x]
        neo += " " * (maxWidth - len(neo))
        res.append(neo)

        return res