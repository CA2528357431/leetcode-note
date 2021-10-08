L = 10
bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

class Solution:
    def findRepeatedDnaSequences(self, s: str) :
        n = len(s)
        if n <= 10:
            return []
        ans = []
        x = 0
        for ch in s[:10 - 1]:
            x = (x << 2)
            x = x|bin[ch]
        cnt = {}
        for i in range(n - 9):
            x = ((x << 2) | bin[s[i + 9]]) & ((1 << (10 * 2)) - 1)
            cnt[x] = cnt.get(x,0)+1
            if cnt[x] == 2:
                ans.append(s[i : i + 10])
        return ans

sol = Solution()
x = sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print(x)