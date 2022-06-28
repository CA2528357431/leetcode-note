class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = area**0.5
        if l%1!=0:
            l = int(l)+1
        else:
            l = int(l)
        while True:
            if area%l==0:
                return [l,area//l]
            else:
                l+=1