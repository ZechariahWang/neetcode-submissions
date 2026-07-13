class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [48,24,12,8]

        res = []

        prefix=1
        prefixes=[1]*len(nums)
        for i in range(len(nums)):
            prefixes[i] = prefix
            prefix *= nums[i]

        suffix = 1
        suffixes=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            suffixes[i] = suffix
            suffix *= nums[i]
            res.append(suffixes[i] * prefixes[i])

        return res[::-1]

            





        