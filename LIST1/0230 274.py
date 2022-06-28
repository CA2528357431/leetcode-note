class Solution:
    def hIndex(self, citations: List[int]) -> int:

        '''
        citations.sort(reverse = True)
        n = len(citations)
        res = 0
        for i in range(n):
            if citations[i]>=i+1:
                res = i+1
            else:
                break
        return res
        '''


        n = len(citations)
        count = [0]*(n+1)
        for item in citations:
            if item>=n:
                count[n]+=1
            else:
                count[item]+=1
        dos = 0
        for i in range(n, -1, -1):
            dos += count[i]
            if dos >= i:
                return i