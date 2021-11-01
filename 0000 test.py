class Solution:
    def minimumOperations(self, nums: List[int], s: int, g: int) -> int:
        used = set()
        cur = [[s, 0]]
        while cur:
            neo = []
            for x,l in cur:
                if x in used:
                    continue
                used.add(x)

                if x == g:
                    return l

                if not (0 <= x <= 1000):
                    continue

                for n in nums:
                    if x + n not in used:
                        neo.append([x+n, l+1])
                    if x - n not in used:
                        neo.append([x-n, l+1])
                    if x ^ n not in used:
                        neo.append([x^n, l+1])
            cur = neo
        return -1