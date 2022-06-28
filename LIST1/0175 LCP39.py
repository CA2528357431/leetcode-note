class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        dict1 = {}
        for x in range(len(source)):
            for y in range(len(source[0])):
                if source[x][y] in dict1:
                    dict1[source[x][y]]+=1
                else:
                    dict1[source[x][y]]=1
        dict2 = {}
        for x in range(len(target)):
            for y in range(len(target[0])):
                if target[x][y] in dict2:
                    dict2[target[x][y]]+=1
                else:
                    dict2[target[x][y]]=1
        res = 0
        for key,value in dict1.items():
            if key not in dict2:
                res+=value
            elif dict2[key]<value:
                res+=(value-dict2[key])
        return res