class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3!=0:
            return []
        res = [num//3-1,num//3,num//3+1]
        return res