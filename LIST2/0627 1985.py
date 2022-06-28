class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        neonums = [int(x) for x in nums]
        neonums.sort(reverse = True)
        return str(neonums[k-1])
