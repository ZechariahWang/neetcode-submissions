class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res = [nums[i], nums[j], nums[k]]
                        result.add(tuple(res))
        
        return [list(i) for i in result]
        