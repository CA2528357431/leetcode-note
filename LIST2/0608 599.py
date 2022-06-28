class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        dic2 = {}
        for i in range(len(list2)):
            dic2[list2[i]] = i

        res = []
        cur = 999999
        for i in range(len(list1)):
            x = list1[i]
            if x in dic2:
                num = dic2[x] + i
                if cur > num:
                    res = [x]
                    cur = num
                elif cur == num:
                    res.append(x)
        return res