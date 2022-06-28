class Solution:
    def countVowelPermutation(self, n: int) -> int:
        cur = [1]*5
        for i in range(n-1):
            neo = [1]*5
            neo[0] = cur[1]+cur[2]+cur[4]
            neo[1] = cur[0]+cur[2]
            neo[2] = cur[1]+cur[3]
            neo[3] = cur[2]
            neo[4] = cur[2]+cur[3]
            cur = neo
        return sum(cur)%1000000007