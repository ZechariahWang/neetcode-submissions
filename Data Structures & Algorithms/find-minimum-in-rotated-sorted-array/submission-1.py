class Solution:
    def findMin(self, nums: List[int]) -> int:
        # approach, binary search
        # we need a target value, it will be nums[r] (target updated after each pass, its dynamic)
        # the reason is because there is a drop between two sub arrays within the nums array, 
        # but despite the drop the second subarray will always be smaller than the first subarray
        # so use that as the target, run binary search, but instead of searching for a value just keep going until theres one value left in the array
        # nums[mid] > nums[r] the val is prob in the first array, so we can just discard that entire half
        # nums[mid] < nums[r] the val might be in the second array, keep it
        # keep doing this until theres only one value left in the array, that value is the answer because its the minimum
        # return that answer

        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid +1
            elif nums[mid] < nums[r]:
                r = mid
        return nums[l]