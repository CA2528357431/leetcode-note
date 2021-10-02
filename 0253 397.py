class Solution:
    def integerReplacement(self, n: int) -> int:
        # dp
        '''
        res = [9999]*(n+1)
        res[1] = 0
        for i in range(2,n+1):
            if i%2==0:
                res[i]=res[i//2]+1
            else:
                minus = res[i-1]+1
                plus = res[(i+1)//2]+1+1
                res[i]=min(plus,minus)
        return res[-1]
        '''

        # 递归
        '''
        if n==1:
            return 0
        elif n%2==1:
            return min(self.integerReplacement(n+1),self.integerReplacement(n-1))+1
        else:
            return self.integerReplacement(n//2)+1
        '''

        # BFS
        '''
        li = [n]
        i = 0
        while True:
            neo = []
            for x in li:
                if x==1:
                    return i
                else:
                    if x%2==0:
                        neo.append(x//2)
                    else:
                        neo.append(x+1)
                        neo.append(x-1)
            li = neo
            i+=1
        '''

        # 尾数判断
        # 尽可能让二进制尾部出现多的0
        i=0
        while True:
            if n==1:
                return 0+i
            elif n==2:
                return 1+i
            elif n==3:
                return 2+i
            else:
                binnum = bin(n)
                if binnum[-2:] == "11":
                    n+=1
                elif binnum[-2:] == "01":
                    n-=1
                else:
                    n = n//2
                i+=1