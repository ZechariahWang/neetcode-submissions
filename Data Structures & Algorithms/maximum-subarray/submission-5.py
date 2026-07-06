class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal=-1000
        currentSub=[]

        if len(nums)==1:
            return nums[0]

        if len(nums)==2:
            return max(nums[0],nums[1])

        for i in range(len(nums)):
            currentSub.append(nums[i])
            for j in range(i+1, len(nums)):
                currentSub.append(nums[j])
                currentSum=sum(currentSub)
                if currentSum > maxVal:
                    maxVal=currentSum
                elif currentSum < maxVal:
                    continue

            currentSub.clear()

        return maxVal

