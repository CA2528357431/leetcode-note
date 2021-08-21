class Solution:
    def longestCommonPrefix(self, strs):
        '''
        cur = strs[0]

        for x in range(1, len(strs)):
            la = cur
            cur = strs[x]
            neo = ""
            l = 0
            while l < len(la) and l < len(cur):
                if la[l] == cur[l]:
                    neo += la[l]
                    l+=1
                else:
                    break
            cur = neo
        return cur
        '''

        if len(strs) == 1:
            return strs[0]
        if len(strs) == 2:
            a = 0
            while a < len(strs[0]) and a < len(strs[1]):
                if strs[0][a] == strs[1][a]:
                    a += 1
                else:
                    break
            return strs[0][:a]
        a = self.longestCommonPrefix(strs[:len(strs) // 2])
        b = self.longestCommonPrefix(strs[len(strs) // 2:])
        res = self.longestCommonPrefix([a, b])
        return res

