class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        stage = 0
        step = 0
        for x in range(len(nums)-1):
            far = max(far,x+nums[x])

            if x==stage:
                step += 1
                stage = far
                
        return step

# stage 记录“阶段”
# 表示前一阶段内元素最远能到的点
# 每遍历完整个stage才对step+1