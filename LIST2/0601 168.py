class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        li = []
        while columnNumber:
            neo = columnNumber % 26
            columnNumber //= 26
            if neo == 0:
                columnNumber -= 1
                li.append("Z")
            else:
                li.append(chr(neo - 1 + ord("A")))

        li.reverse()

        return "".join(li)