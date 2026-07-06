class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,1,2,3,4]
        #      j
        #    k 

        if not nums:
            return 0

        j, k = 1, 0
        i = 0 # num of duplicates
        while j < len(nums) and k < len(nums):
            print(f"i, j, k: {i, j, k}")
            if nums[j] == nums[k]:
                i += 1
                j+=1 
            else:
                k += 1
                nums[k] = nums[k+1]
                
            if j == k:
                j += 1

        return k+1

        

