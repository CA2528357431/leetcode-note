class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        alpha = "abcdefghijklmnopqrstuvwxyz"

        def ind(c):
            return ord(c) - ord("a")

        def get(s):
            res = 0
            for c in s:
                res = res | (1 << ind(c))
            return res

        st = get("act")
        sli = set()
        for w in startWords:
            nn = get(w)
            for add in alpha:
                if add in w:
                    continue
                neo = nn | get(add)
                sli.add(neo)

        cnt = 0
        for w in targetWords:
            neo = get(w)
            if neo in sli:
                cnt += 1

        return cnt