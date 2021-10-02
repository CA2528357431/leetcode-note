class Solution:
    def toHex(self, num: int) -> str:
        CONV = "0123456789abcdef"
        res = ""
        for _ in range(8):
            res = CONV[num%16]+res
            print(res[0],num%16)
            num //= 16
            if not num:
                break
        return res