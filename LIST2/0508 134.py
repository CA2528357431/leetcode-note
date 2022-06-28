class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 如果从a到不了b，那ab之间的点出发一定到不了b
        '''
        n = len(gas)
        i = 0
        while i<n:
            ii = i
            cur = 0
            while ii<i+n:
                j = ii%n
                cur = cur+gas[j]-cost[j]
                if cur<0:
                    break
                else:
                    ii+=1
            j = ii%n
            if ii==i+n:
                return j
            if j<i:
                return -1
            i = (ii%n)+1

        return -1
        '''

        # 只有总油不足才无解
        if sum(gas) < sum(cost):
            return -1

        cursum = 0
        res = 0
        for i in range(len(cost)):
            cursum += gas[i] - cost[i]
            # 进行不下去，更新res
            if cursum < 0:
                cursum = 0
                res = i+1
        return res