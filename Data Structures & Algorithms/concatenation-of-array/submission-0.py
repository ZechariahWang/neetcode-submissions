class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # strategy: mka e a copy of nums
        # concatenate nums + copy o fnums into a new array
        # return new array

        copy_nums = [nums[i] for i in range(len(nums))]
        res = nums+ copy_nums
        return res

        