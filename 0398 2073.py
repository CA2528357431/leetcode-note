class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        res = 0
        t = tickets[k]
        for i in range(n):
            if tickets[i] < t:
                res += tickets[i]
            else:
                if i <= k:
                    res += t
                else:
                    res += (t - 1)
        return res

