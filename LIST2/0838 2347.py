class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        j = True
        for i in range(4):
            if suits[i] != suits[-1]:
                j = False
        if j == True:
            return "Flush"

        ranks.sort()

        same = 1
        cur = 1
        for i in range(1, 5):
            if ranks[i] == ranks[i - 1]:
                cur += 1
                same = max(same, cur)
            else:
                cur = 1
        if same >= 3:
            return "Three of a Kind"
        elif same == 2:
            return "Pair"
        else:
            return "High Card"
