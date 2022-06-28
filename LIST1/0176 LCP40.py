class Solution:
    def maxmiumScore(self, cards, cnt: int) -> int:
        '''
        single = []
        double = []
        for x in cards:
            if x % 2 == 0:
                double.append(x)
            else:
                single.append(x)
        single.sort(reverse=True)
        double.sort(reverse=True)

        sums = [0]
        sumd = [0]
        for x in single:
            sums.append(x + sums[-1])
        for x in double:
            sumd.append(x + sumd[-1])

        res = 0

        for s in range(0, min(len(single), cnt) + 1, 2):
            if cnt - s < len(sumd):
                res = max(res, sums[s] + sumd[cnt - s])

        return res
        '''

        sums = [0]
        sumd = [0]
        cards.sort(reverse=True)
        for x in cards:
            if x % 2 == 0:
                sumd.append(x + sumd[-1])
            else:
                sums.append(x + sums[-1])

        res = 0

        for s in range(0, min(len(sums), cnt+1), 2):
            if cnt - s < len(sumd):
                res = max(res, sums[s] + sumd[cnt - s])

        return res