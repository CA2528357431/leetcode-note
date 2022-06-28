class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = 99999999
        dic = {}

        for i in range(len(cards)):
            c = cards[i]
            if c not in dic:
                dic[c] = i
            else:
                res = min(res, i - dic[c] + 1)
                dic[c] = i
        if res == 99999999:
            return -1
        return res

