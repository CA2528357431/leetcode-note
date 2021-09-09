class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}

        for string in strs:
            li = list(string)
            li.sort()
            neo = "".join(li)
            if neo in dic:
                dic[neo].append(string)
            else:
                dic[neo] = [string]

        res = [value for _, value in dic.items()]

        return res