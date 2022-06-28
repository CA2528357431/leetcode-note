class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        judge = [False]*(len(s)+1)
        judge[0] = True
        for x in range(len(s)):
            for y in range(x,len(s)):
                if judge[x] and (s[x:y+1] in wordDict):
                    judge[y+1] = True
        return judge[-1]