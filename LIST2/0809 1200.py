class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        cur = arr[-1]-arr[0]
        for i in range(len(arr)-1):
            delta = arr[i+1]-arr[i]
            if delta<cur:
                res = [[arr[i],arr[i+1]]]
                cur = delta
            elif delta==cur:
                res.append([arr[i],arr[i+1]])
        return res