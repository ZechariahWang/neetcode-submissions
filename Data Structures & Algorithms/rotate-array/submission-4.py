class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # [1,2,3,4] k=2 -> [3,4,1,2]
        # [1,2,3,4,5,6,7,8] k = 4 -> [5,6,7,8,1,2,3,4]

        # strat: loop through the entire array UP until len(nums)-k
        # for vevery value, get it and also get the value k steps over
        # Swap the two values

        # for i in range(len(nums)-k):
        #     temp = nums[i]
        #     nums[i] = nums[i+k]
        #     nums[i+k] = temp

        # new strat:

        if k > len(nums):
            k = k % len(nums)

        nums.reverse()
        nums[0:k] = nums[0:k][::-1]
        nums[k:len(nums)] = nums[k:len(nums)][::-1]

