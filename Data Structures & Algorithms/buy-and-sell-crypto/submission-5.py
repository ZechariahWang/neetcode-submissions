class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # approach:
        # loop through each element i
        # loop through each element j
        # take element j - element i
        # have a max value var, update it if current value > max value
        
        max_value = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                current_value = prices[j] - prices[i]
                max_value = max(max_value, current_value)

        return max_value