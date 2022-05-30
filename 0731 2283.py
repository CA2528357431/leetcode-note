class Solution:
    def digitCount(self, num: str) -> bool:
        n = len(num)
        dic = {}
        for i in range(n):
            c = num[i]
            if c not in dic:
                dic[c] = 0
            dic[c] += 1

        for i in range(n):
            c = int(num[i])
            if str(i) not in dic:
                if c != 0:
                    return False
            else:
                if c != dic[str(i)]:
                    return False
        return True