class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        num_e = -1
        num_p = -1
        nums = "1234567890"
        for i in range(len(s)):
            if num_e>=0:
                if s[i] in nums:
                    continue
                elif s[i] in "+-":
                    if i==num_e+1 and i<len(s)-1:
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                if s[i] in nums:
                    continue
                elif s[i] in "+-":
                    if i==0:
                        continue
                    else:
                        return False
                elif s[i] == ".":
                    if num_p<0 and ((i-1>=0 and s[i-1] in nums) or (i+1<len(s) and s[i+1] in nums)):
                        num_p = i
                    else:
                        return False
                elif s[i] in "Ee":
                    if num_e<0 and i>0 and (s[i-1] in nums or s[i-1]==".") and i+1<len(s):
                        num_e = i
                    else:
                        return False
                else:
                    return False


        return True