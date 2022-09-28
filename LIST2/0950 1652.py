class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        neo = [0]*n
        for i in range(n):
            if k<0:
                for j in range(i+k,i):
                    j = (j+n)%n
                    neo[i]+=code[j]
            elif k>0:
                for j in range(i+1,i+k+1):
                    j = j%n
                    neo[i]+=code[j]
        return neo