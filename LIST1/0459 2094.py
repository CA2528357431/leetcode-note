class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        n = len(digits)
        res = []
        for x in range(n):
            if x>0 and digits[x-1]==digits[x]:
                continue
            if digits[x]==0:
                continue
            for y in range(n):
                if x==y:
                    continue
                if y>0 and y!=x+1 and digits[y-1]==digits[y]:
                    continue
                if digits[y]%2!=0:
                    continue
                for z in range(n):
                    if x==z or y==z:
                        continue
                    if z>0 and z!=y+1 and z!=x+1 and digits[z-1]==digits[z]:
                        continue
                    cur=digits[x]*100+digits[z]*10+digits[y]
                    res.append(cur)
        res.sort()
        return res