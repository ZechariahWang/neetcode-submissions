class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l]+nums[r]+nums[i]==0:
                    if [nums[l],nums[r],nums[i]] in res:
                        l +=1 
                        continue
                    res.append([nums[l],nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l]+nums[r]+nums[i] < 0:
                    l += 1
                elif nums[l]+nums[r]+nums[i] > 0:
                    r -= 1

        return res


