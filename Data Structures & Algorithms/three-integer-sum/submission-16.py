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
                    res.append([nums[l],nums[r],nums[i]])
                    l += 1
                    while l<r and nums[l]==nums[l-1]:
                        l += 1

                if current < 0:
                    l += 1
                if current > 0:
                    r -= 1

        return res



        