class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1]))
        cur = 1
        la = pairs[0][1]
        for i in range(1, len(pairs)):
            s, e = pairs[i]
            if s > la:
                la = e
                cur += 1

        return cur
