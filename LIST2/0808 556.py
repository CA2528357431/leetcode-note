class Solution:
    def nextGreaterElement(self, n: int) -> int:
        string = list(str(n))
        ii = -1
        for i in range(len(string) - 1):
            if int(string[i]) < int(string[i + 1]):
                ii = i
        if ii == -1:
            return -1

        ai = ii + 1
        for i in range(ii + 1, len(string)):
            if int(string[ii]) < int(string[i]) < int(string[ai]):
                ai = i
        string[ai], string[ii] = string[ii], string[ai]
        l = "".join(string[:ii + 1])
        string = string[ii + 1:]
        string.sort()
        r = "".join(string)
        res = int(l + r)
        if res > (2 ** 31 - 1):
            return -1
        return res