class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        # 二分查找
        '''
        houses.sort()
        heaters.sort()
        def find(house):
            if house<=heaters[0]:
                return heaters[0]-house
            if house>=heaters[-1]:
                return house-heaters[-1]
            n = len(heaters)
            l = 0
            r = n-1
            while l<r:
                mid = (l+r)//2+1
                if heaters[mid]<=house:
                    l = mid
                else:
                    r = mid-1
            return min(abs(house-heaters[l]),abs(house-heaters[l+1]))
        res = 0
        for h in houses:
            res = max(res,find(h))

        return res
        '''

        # 双指针
        houses.sort()
        heaters.sort()

        res = 0

        he = 0
        for ho in houses:
            while heaters[he] <= ho and he < len(heaters) - 1:
                he += 1
            dis = min(abs(ho - heaters[he]), abs(ho - heaters[he - 1]))
            res = max(res, dis)

        return res