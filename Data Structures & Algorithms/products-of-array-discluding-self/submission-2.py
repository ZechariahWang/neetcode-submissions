class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            total_sum = 1
            for j in range(len(nums)):
                if i == j: 
                    continue
                total_sum = total_sum * nums[j]
            res.append(total_sum)

        return res



        