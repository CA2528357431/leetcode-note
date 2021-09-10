class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0
        s = sum(chalk)
        n = len(chalk)
        k = k % s
        while k >= chalk[i % n]:
            k -= chalk[i % n]
            i += 1

        return i % n