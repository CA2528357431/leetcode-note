class Solution:
    def compress(self, chars) :
        w = 0
        count = 1
        cur = chars[0]
        chars.append("")
        for r in range(1, len(chars)):
            if chars[r] != cur:
                chars[w] = cur
                w += 1
                if count > 1:
                    for num in str(count):
                        chars[w] = num
                        w += 1
                cur = chars[r]
                count = 1
            else:
                count += 1
        while len(chars) > w:
            chars.pop()

        return w

    # r针读取 w针写入