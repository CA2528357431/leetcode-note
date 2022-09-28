class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {}
        for x in pieces:
            dic[x[0]] = x

        i = 0
        while i < len(arr):
            if arr[i] not in dic:
                return False

            for x in dic[arr[i]]:
                if x == arr[i]:
                    i += 1
                else:
                    return False

        return True