class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # approach:
        # start with a pointer i
        # we consider that as the sell point
        # this means the only potential buy points are to the left of the sell point
        # compare all of those and update
        # keep increasing i accordingly
        
        max_value = 0
        min_price = prices[0]
        for i in range(len(prices)):
            
            min_price = min(min_price, prices[i])

            current_value = prices[i] - min_price
            max_value = max(current_value, max_value)

        return max_value