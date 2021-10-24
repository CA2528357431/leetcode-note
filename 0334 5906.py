class Solution:
    def countValidWords(self, sentence: str) -> int:
        def deal(x):

            a = "!.,"
            b = "-"
            c = "1234567890"
            if len(x) == 1:
                if x == b or x in c:
                    return False
                else:
                    return True

            if x[0] == b or x[0] in c or x[0] in a or x[-1] == b or x[-1] in c:
                return False

            link = 0
            for i in range(1, len(x) - 1):
                ch = x[i]
                if ch == b:
                    link += 1
                    if link > 1:
                        return False
                elif ch in c or ch in a:
                    return False

            if x[-1] in a and x[-2] == "-":
                return False

            return True

        li = sentence.split()
        num = 0
        for x in li:
            if deal(x):
                num += 1
        return num