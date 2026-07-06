class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        baseNum = nums[0]

        for i in range(1, len(nums), 1):
            if baseNum + nums[i] == target:
                return [0, i]

        