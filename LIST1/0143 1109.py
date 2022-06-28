class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        '''
        res = [0]*n
        for booking in bookings:
            for x in range(booking[0],booking[1]+1):
                res[x-1] += booking[2]
        return res
        '''


        # 差分法

        res = [0] * n
        for l, r, num in bookings:
            res[l - 1] += num
            if r + 1 <= n:
                res[r - 1 + 1] -= num

        # 本次处理之后，每一位的数据，实质上是表示
        # 最终结果的 从此（包括）开始之后的所有位 都需要加上这个数字
        # 也可以看作是res[i]-res[i-1]
        # 如[1,2,3,-2] ，最总结果是(1,3,6,4)
        # 这样就不需要遍历每个booking中的l和r

        for x in range(1, n):
            res[x] += res[x - 1]

        # 由差分数组转化成结果

        return res
