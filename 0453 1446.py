class Solution:
    def maxPower(self, s: str) -> int:
        energy = 1
        cur_e = 1
        cur = s[0]
        for i in range(1,len(s)):
            if cur!=s[i]:
                cur = s[i]
                energy = max(energy,cur_e)
                cur_e=1
            else:
                cur_e+=1
        return max(energy,cur_e)