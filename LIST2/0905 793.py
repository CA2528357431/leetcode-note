class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def find(x):
            find = 5
            cnt = 0
            while find <= x:
                cnt += x // find
                find *= 5
            return cnt

        def get(limit):
            l = 0
            r = 5 * limit
            while l < r:
                mid = (l + r) // 2
                if find(mid) < limit:
                    l = mid + 1
                else:
                    r = mid
            return l

        big = get(k + 1)
        sml = get(k)
        return big - sml