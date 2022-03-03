class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = []
        for line in bank:
            num = 0
            for c in line:
                if c == "1":
                    num += 1
            if num:
                count.append(num)
        res = 0
        for i in range(len(count) - 1):
            res += count[i] * count[i + 1]
        return res
