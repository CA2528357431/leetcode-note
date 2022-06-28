class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        li = []
        i = 0
        j = 0
        m = len(word1)
        n = len(word2)
        while i<m or j<n:
            if i==m:
                li.append(word2[j])
                j+=1
            elif j==n:
                li.append(word1[i])
                i+=1
            else:
                if i==j:
                    li.append(word1[i])
                    i+=1
                else:
                    li.append(word2[j])
                    j+=1
        return "".join(li)
