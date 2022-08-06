class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        n = len(tasks)
        dic = {}

        res = 0
        for i in range(n):
            todo = tasks[i]
            if todo not in dic:
                dic[todo] = res + space + 1
                res += 1
            else:
                early = dic[todo]
                if early > res:
                    res = early + 1
                    dic[todo] = early + space + 1
                else:
                    dic[todo] = res + space + 1
                    res += 1
        return res

