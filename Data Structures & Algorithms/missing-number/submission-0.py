class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet=set(nums)
        for i in range(len(numSet)):
            if i not in numSet:
                return i
        return 0