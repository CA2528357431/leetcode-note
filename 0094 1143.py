class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cur = [0]*(len(text1)+1)
        for x in range(len(text2)):
            la = cur.copy()
            for y in range(len(text1)):
                if text1[y]==text2[x]:
                    cur[y+1]=la[y]+1
                else:
                    cur[y+1] = max(cur[y],la[y+1])
        return cur[-1]