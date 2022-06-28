class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        time=minutesToTest//minutesToDie
        n=math.log(buckets)/math.log(time+1)
        if n%1==0:
            return int(n)
        else:
            return int(n)+1

        # 猪的个数代表维度
        # time+1代表维度的边长
