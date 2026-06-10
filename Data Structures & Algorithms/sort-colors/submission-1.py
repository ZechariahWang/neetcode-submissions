class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def mergeSort(nums, l, m, r):
            left = nums[l:m+1]
            right = nums[m+1: r+1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] < right[k]:
                    nums[i] = left[j]
                    j+=1 
                    i +=1
                else:
                    nums[i] = right[k]
                    k += 1
                    i += 1
            
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i +=1 

            while k < len(right):
                nums[i] = right[k]
                k +=1 
                i +=1

        def merge(nums, l, r):
            if l >= r:
                return
            m = (l+r) // 2
            merge(nums, l, m)
            merge(nums, m+1, r)
            mergeSort(nums, l, m, r)

        merge(nums, 0, len(nums)-1)
        