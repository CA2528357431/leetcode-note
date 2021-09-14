class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        '''
        res = ""
        for x in dictionary:
            i = 0
            j = 0
            while i < len(s) and j < len(x):
                if s[i] == x[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(x):
                if j > len(res) or len(res) == j and x < res:
                    res = x
        return res
        '''


        '''
        dictionary.sort(key=lambda x: (-len(x), x))

        for x in dictionary:
            i = 0
            j = 0
            while i < len(s) and j < len(x):
                if s[i] == x[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(x):
                return x
        return ""
        '''

        # 动态规划

        res = [{} for _ in range(len(s)+1)]
        for i in range(len(s)-1,-1,-1):
            res[i] = res[i+1].copy()
            if s[i] in res[i]:
                res[i][s[i]] = min(res[i][s[i]],i)
            else:
                res[i][s[i]] = i
        result = ""
        for word in dictionary:
            i = 0
            j = 0
            while i<len(s) and j<len(word):
                if word[j] in res[i]:
                    i = res[i] + 1
                    j += 1
                else:
                    break
            if j==len(word):
                if len(word)>len(result) or len(word)==len(result) and word<result:
                    result = word
        return result



