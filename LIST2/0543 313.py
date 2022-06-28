class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        '''
        m = len(primes)
        index = [0] * m
        res = [1] * n
        for i in range(1, n):
            change = 9999999999
            jj = [-1]
            for j in range(m):
                neo = primes[j] * res[index[j]]
                if neo < change:
                    change = neo
                    jj = [j]
                elif neo == change:
                    jj.append(j)
                    # 可能由个方案值一样

            res[i] = change
            for j in jj:
                index[j] += 1

        return res[-1]
        '''

        # 优化
        m = len(primes)
        index = [0] * m
        res = [1] * n
        nums = primes.copy()
        for i in range(1, n):
            change = min(nums)
            res[i] = change
            for j in range(m):
                if nums[j] == change:
                    index[j] += 1
                    nums[j] = res[index[j]] * primes[j]

        return res[-1]