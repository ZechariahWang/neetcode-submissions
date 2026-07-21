class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # approach: prefix + suffix sum
        # loop through the list one pass forwards, multiple prefix array val at index i by the prefix var, update prefix to be current num
        # loop through the list one pass backwards, multiple suffix array val at index i by the suffix var, update suffix to be current num
        # at the very end, multiply the values of the prefix array by the suffix array, store in a res array, return res

        # [1,2,3,4]
        # prefix=[]
        # [24,12,8,6]

        res = [1]*len(nums)

        prefixes=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            prefixes[i] = prefix
            prefix *= nums[i]

        suffixes = [1]*len(nums)
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            suffixes[i] = suffix
            suffix *= nums[i]
            res[i] = suffixes[i] * prefixes[i]

        return res

        