class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        status = 1<<n

        # 压缩状态

        nums = [n]*status
        nums[0] = 1
        lasts = [sessionTime]*status
        lasts[0] = 0

        for i in range(1,status):
            for j in range(n):
                todo = i&(1<<(n-1-j))
                if todo:
                    pre = i-(1<<(n-1-j))
                    last = lasts[pre]+tasks[j]
                    num = nums[pre]
                    if last>sessionTime:
                        num+=1
                        last=tasks[j]

                    if num<nums[i] or num==nums[i] and last<lasts[i]:
                        nums[i] = num
                        lasts[i] = last

        return nums[-1]
