class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        smallest=0
        counter=1
        for i in range(len(nums)):
            candidates=[]
            for j in range(i+1, len(nums)):
                candidates.append(nums[j])
            if candidates:
                number=min(candidates)
            if number>smallest:
                smallest=number
                counter+=1
                print(number)
        return counter

