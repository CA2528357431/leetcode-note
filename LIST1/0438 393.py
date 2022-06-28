class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        def getLen(i):
            c = 0
            cur = data[i]
            while cur & 0b10000000:
                c += 1
                cur = (cur << 1) % 256
            return c

        n = len(data)
        for i in range(n):
            data[i] = data[i] % 256

        cap = 0
        for i in range(n):
            if cap:
                if getLen(i) != 1:
                    return False
                cap -= 1
            else:
                l = getLen(i)
                if l > 4 or l == 1:
                    return False

                elif l == 0:
                    continue
                else:
                    cap = l - 1
            print(cap)
        return cap == 0