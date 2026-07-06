class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low, mid, high = 0,0, len(nums)-1

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid +=1
            elif nums[i] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        