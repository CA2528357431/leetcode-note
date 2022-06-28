class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for x in range(n-3):
            if x!=0 and nums[x]==nums[x-1]:
                continue
            if nums[x] + nums[x + 1] + nums[x + 2] + nums[x + 3] > target:
                break
            if nums[x] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for y in range(x+1,n-2):
                if y!=x+1 and nums[y]==nums[y-1]:
                    continue
                # 剪枝
                # 如果加入该桶等效于加入上一个桶，就跳过
                if nums[x] + nums[y] + nums[y + 1] + nums[y + 2] > target:
                    break
                if nums[x] + nums[y] + nums[n - 1] + nums[n - 2] < target:
                    continue
                l = y+1
                r = n-1
                while l<r:
                    if nums[x]+nums[y]+nums[l]+nums[r]>target:
                        r-=1
                    elif nums[x]+nums[y]+nums[l]+nums[r]<target:
                        l+=1
                    else:
                        res.append([nums[x],nums[y],nums[l],nums[r]])
                        r-=1
                        l+=1
                        while nums[r]==nums[r+1] and r-1>=l:
                            r-=1
                        while nums[l]==nums[l-1] and l+1<=r:
                            l+=1
        return res

#   优化判定
#   最小也大于tar，由于此后只会更大break
#   if nums[x] + nums[x + 1] + nums[x + 2] + nums[x + 3] > target:
#       break
#   最大也小于tar，由于此后可能更大continue跳过当前
#   if nums[x] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
#       continue
#   这种操作数据越大越有效，如果数据小还会起反效果

