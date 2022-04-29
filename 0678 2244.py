class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        n = 0
        dic = {}
        for c in tasks:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        for k in dic:
            v = dic[k]
            if v==1:
                return -1
            n += (v-1)//3+1
        return n