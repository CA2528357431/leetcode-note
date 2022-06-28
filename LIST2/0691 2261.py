class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        mat = [0] * n
        if nums[0] % p == 0:
            mat[0] = 1
        for i in range(1, n):
            mat[i] = mat[i - 1]
            if nums[i] % p == 0:
                mat[i] += 1
        total = mat[-1]
        res = 0
        used = set()
        for s in range(n):
            i = s
            neg = 0
            j = 0
            if nums[s] % p == 0:
                j = 1
            while i < n and mat[i] - (mat[s] - j) <= k:
                i += 1
                t = tuple(nums[s:i])
                if t in used:
                    neg += 1
                else:
                    used.add(t)

            res += i - s
            res -= neg
        return res
