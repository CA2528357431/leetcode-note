class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)

        l = n // 20
        r = n // 20 * 19
        res = 0
        for i in range(l, r):
            res += arr[i]
        res = res / (r - l)
        return res