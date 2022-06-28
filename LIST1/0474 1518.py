class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        '''
        def ez(num):
            if num<numExchange:
                return 0
            re=num%numExchange
            ne=num//numExchange
            return ne+ez(re+ne)
        return numBottles+ez(numBottles)
        '''
        res = 0
        cur = numBottles
        while cur >= numExchange:
            drink = cur - cur % numExchange
            other = cur % numExchange
            res += drink
            cur = drink // numExchange + other

        return res + cur