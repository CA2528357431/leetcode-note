class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # dp
        '''
        res = [[] for _ in range(target+1)]
        res[0] = [[]]
        for item in candidates:
            for tar in range(target+1):
                if tar-item>=0:
                    for neo in res[tar-item]:
                        li = neo.copy()
                        li.append(item)
                        res[tar].append(li)

        return res[-1]
        '''

        # 回溯

        res = []
        path = []
        def do(path,l,tar):
            if tar==0:
                res.append(path.copy())

            for i in range(l,len(candidates)):
                if candidates[i]<=tar:
                    path.append(candidates[i])
                    do(path,i,tar-candidates[i])
                    path.pop()
            # 从l开始代表着path之前的元素的index都在l以及l之前
            # candidates = [2,3,5] 时
            # path的形式应该 [2,2,3,3,3,5,5]

        do(path,0,target)
        return res