class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # strategy: mka e a copy of nums
        # concatenate nums + copy o fnums into a new array
        # return new array

        copy = nums
        final_list = nums + copy
        return final_list

        