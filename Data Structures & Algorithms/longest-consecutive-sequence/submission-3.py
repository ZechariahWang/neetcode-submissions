class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach: loop through the entire array (i)
        # loop through the entire array again (j)
        # for each number, check if n+1 exists at all inside the array
        # if it does, add that number to a res array
        # at the very end return the res array
        global_res=0
        num_set = set(nums)
        for n in num_set:
            if n-1 not in num_set:
                current_res=1
                while n+current_res in num_set:
                    current_res += 1

                if current_res > global_res:
                    global_res = current_res

        return global_res



                



                