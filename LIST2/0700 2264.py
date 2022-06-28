class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cur = ""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                if not cur:
                    cur = num[i]
                elif int(cur)<int(num[i]):
                    cur = num[i]
        return cur*3
