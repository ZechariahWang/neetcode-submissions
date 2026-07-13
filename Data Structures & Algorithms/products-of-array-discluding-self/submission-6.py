class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [48,24,12,8]

        res = [1] * len(nums)

        prefix=1
        prefixes=[1]*len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # prefixes=[1,1,2,8]

        suffix = 1
        suffixes=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            res[i] = suffix * res[i]
            suffix *= nums[i]
        
        # suffixes=[48,24,6,1]

        return res

            





        