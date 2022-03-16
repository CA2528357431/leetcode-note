class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        find = []
        n = len(nums)
        for x in range(n):
            if nums[x] == key:
                l = max(x - k, 0)
                r = min(x + k, n - 1)
                if not find:
                    find.append([l, r])
                else:
                    ll, rr = find[-1]
                    if rr >= l - 1:
                        find[-1][1] = r
                    else:
                        find.append(l, r)
        res = []
        for l, r in find:
            for x in range(l, r + 1):
                res.append(x)
        return res
