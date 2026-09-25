class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # approach: use prefix and suffix 
        # first pass prefix, mulitply by all numbers ahead and append to prefix arr
        # second pass suffix, multplyi by all numbers behind and append to suffix arr
        # append to res arr prefix * suffix

        res = [1] * len(nums)

        prefixes = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            prefixes[i] *= prefix
            prefix *= nums[i]

        suffixes = [1] * len(nums)
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            suffixes[i] *= suffix
            suffix *= nums[i]
            res[i] = prefixes[i] * suffixes[i]

        return res
        