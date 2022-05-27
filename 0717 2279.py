class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        li = [capacity[i]-rocks[i] for i in range(n)]
        li.sort()
        cnt = 0
        for c in li:
            if c<=additionalRocks:
                cnt+=1
                additionalRocks-=c
            else:
                break
        return cnt