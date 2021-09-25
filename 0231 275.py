class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
        l = 0
        r = n - 1
        while l != r:
            mid = (l + r) // 2
            h = n - mid
            if h <= citations[mid]:
                r = mid
            else:
                l = mid + 1
        h = n - l

        if h <= citations[l]:
            return h

        return 0