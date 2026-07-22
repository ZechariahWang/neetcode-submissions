class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        res=[]

        for i in range(len(nums)):
            if i>0 and nums[i] ==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                current = nums[l] + nums[r] + nums[i]
                if current == 0:
                    if [nums[l],nums[r],nums[i]] in res:
                        l += 1
                        continue
                    res.append([nums[l],nums[r],nums[i]])
                    l += 1
                    r -= 1
                if current < 0:
                    l += 1
                if current > 0:
                    r -= 1

        return res



        