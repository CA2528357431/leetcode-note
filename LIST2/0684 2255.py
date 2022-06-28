class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        def check(small,big):
            if len(small)>len(big):
                return False
            for i in range(len(small)):
                if small[i]!=big[i]:
                    return False
            return True
        cnt = 0
        for w in words:
            if check(w,s):
                cnt+=1
        return cnt