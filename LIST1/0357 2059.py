class Solution:
    def minimumOperations(self, nums: List[int], s: int, g: int) -> int:
        used = {s}
        cur = [[s, 0]]
        while cur:
            neo = []
            for x,l in cur:
                for n in nums:
                    for xx in (x + n,x - n,x ^ n):
                        if xx not in used:
                            if xx==g:
                                return l+1
                            if not (0 <= xx <= 1000):
                                continue
                            neo.append([xx, l+1])
                            used.add(xx)
            cur = neo
        return -1

    # 这也能广度优先.....