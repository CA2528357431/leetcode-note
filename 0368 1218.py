class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dic = {}

        for x in arr:
            if x - difference in dic:
                dic[x] = dic[x - difference] + 1
            else:
                dic[x] = 1

        return max(dic.values())