class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # approach: use a max heap
        # turn a min heap into a max heap by converitng all values in nums into negative numbers
        # declare a counter var
        # loop through the entire max heap
        # through each loop, pop the top element off of the max heap
        # through each iteration increase counter 
        # if counter == k: return the current popped value but negative, exit loop
        # time complexity: O(n+klogn) space complexity: O(n)

        if not nums:
            return 

        nums = [-num for num in nums]
        heapq.heapify(nums)

        value = 0
        for i in range(k):
            value = heapq.heappop(nums)

        return -value
