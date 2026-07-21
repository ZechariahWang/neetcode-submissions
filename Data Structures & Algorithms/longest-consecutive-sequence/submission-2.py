class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach: loop through the entire array (i)
        # loop through the entire array again (j)
        # for each number, check if n+1 exists at all inside the array
        # if it does, add that number to a res array
        # at the very end return the res array

        global_res=1

        if nums == []:
            return 0

        for i in range(len(nums)):
            local_res=1
            current = nums[i]
            while (current+1 in nums):
                local_res += 1
                current+=1 
                if local_res > global_res:
                    global_res = local_res

        return global_res



                