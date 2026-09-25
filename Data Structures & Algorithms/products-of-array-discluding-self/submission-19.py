class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zc = 1,0

        for num in nums:
            if num:
                prod *= num
            else:
                zc += 1

        if zc > 1: return [0] * len(nums)

        res = [0] * len(nums)

        for i,n in enumerate(nums):
            if zc: res[i] = 0 if n else prod
            else:
                res[i] = prod//n
            
        return res