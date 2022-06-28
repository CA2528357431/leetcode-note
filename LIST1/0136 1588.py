class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        if n==1:
            return arr[0]
        res = [0]*n
        res[0] = arr[0]
        res[1] = arr[1]
        s = res[0]+res[1]
        for x in range(2,n):
            res[x]=res[x-2]+(x//2)*(arr[x]+arr[x-1])+arr[x]
            s+=res[x]
        return s