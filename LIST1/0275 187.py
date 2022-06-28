class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''
        n = len(s)
        dic = {}
        res = []
        for i in range(0,n-9):
            string = s[i:i+10]
            dic[string] = dic.get(string,0)+1
            if dic[string]==2:
                res.append(string)

        return res
        '''
        # 通过二进制表示编码
        over = (1 << (10 * 2)) - 1
        n = len(s)
        if n <= 10:
            return []
        dic = {"A":0,"C":1,"G":2,"T":3}
        num = 0
        for i in range(10):
            num = num<<2
            num = num|dic[s[i]]
        re = {num:1}
        res = []
        for i in range(10,n):
            num = num<<2
            num = num | dic[s[i]]
            num = num&over
            re[num] = re.get(num,0)+1
            if re[num] ==2:
                res.append(s[i-9:i+1])
        return res