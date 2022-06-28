class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dou = {}
        sin = {}

        dic = {}

        for w in words:

            if w not in dic:
                dic[w] = 0
            dic[w] += 1

        for w in words:

            if w in sin or w in dou:
                continue

            if w[0] == w[1]:

                sin[w] = dic[w]
            else:
                num = min(dic[w], dic.get(w[1] + w[0], 0))
                if num:
                    dou[w] = num
                    dou[w[1] + w[0]] = num

        smaxs = 0
        smaxd = 0
        for k in sin:
            if sin[k] % 2 == 1:
                if sin[k] > smaxs:
                    smaxd += max(smaxs - 1, 0)
                    smaxs = sin[k]
                else:
                    smaxd += sin[k] - 1
            else:
                smaxd += sin[k]

        res = smaxd + smaxs
        for k in dou:
            res += dou[k]

        return res * 2


