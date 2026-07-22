class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        l = 0
        r = len(height)-1

        while l < r:
            current_height = min(height[l], height[r])
            current_area = current_height * (r-l)

            # we inrease the pointer with the lower height
            # this is bc say height[l+1] is somehow the same or smaller, we know the width will between r and l will decrease by at least 1
            # so no matter what, area will be decreasing, so it doesnt rlly make a difference
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            max_area = max(max_area, current_area)

        return max_area
        