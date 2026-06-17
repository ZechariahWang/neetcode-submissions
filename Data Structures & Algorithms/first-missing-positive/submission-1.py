class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing_num = 1
        for i in range(len(nums)):
            if missing_num in nums:
                missing_num += 1
            else:
                return missing_num
        
        return missing_num