class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,1,2,3,4]
        #        j
        #      k 

        # [1,2,3,3,4]

        if not nums:
            return 0

        j, k = 0, 1
        while j < len(nums) and k < len(nums):
            print(f"j, k: {j, k}")
            if nums[j] == nums[k]:
                k+=1 
            else:
                j += 1
                nums[j] = nums[j+1]
                
            if j == k:
                k += 1

        return j+1

        

