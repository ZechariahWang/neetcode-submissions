class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0

        for i in range(len(height)):
            for j in range(i, len(height)):
                current_height = min(height[i], height[j])
                current_area = current_height * (j-i)
                max_area = max(max_area, current_area)

        return max_area
        