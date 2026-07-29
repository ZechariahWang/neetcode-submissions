class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # approach, binary search
        # run binary search with l, r once you find m, you have two subarrays
        # try to find which subarray is sorted, once you find the one that is sorted check if the target value is in there
        # if its not, check the other unsorted array
        # if ur at the unsorted array, repeat the whole process where u find the mid, and check the sorted array first then the unsorted one

        # first pass
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        # second pass:
        pivot = l
        l, r = 0, len(nums)-1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1

        return -1
