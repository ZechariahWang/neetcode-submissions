class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        l = 0
        r = len(height)-1

        while l < r:
            current_height = min(height[l], height[r])
            current_area = current_height * (r-l)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            max_area = max(max_area, current_area)

        return max_area
        