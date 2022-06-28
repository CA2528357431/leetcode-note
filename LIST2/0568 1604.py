class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def gettime(string):
            li = string.split(":")
            h, m = int(li[0]), int(li[1])
            return h * 60 + m

        def deal(li):
            l = len(li)
            if l < 3:
                return True
            li.sort()
            for i in range(1, l - 1):
                if li[i + 1] - li[i - 1] <= 60:
                    return True
            return False

        n = len(keyName)
        dic = {}
        for i in range(n):
            name = keyName[i]
            time = gettime(keyTime[i])
            if name not in dic:
                dic[name] = []
            dic[name].append(time)

        res = []
        for name in dic:
            if deal(dic[name]):
                res.append(name)
        res.sort()
        return res