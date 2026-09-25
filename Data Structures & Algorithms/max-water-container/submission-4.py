class Solution:
    def maxArea(self, height: List[int]) -> int:
        # approach: run two pointers
        # l = 0, r = len(height)-1
        # get the area given by the pointers via min(l, r) * (r-l)
        # compare it to max area, update max
        # depending on which bar is shorter, move that one
        # if l is shorter, move l up, if r is shorter move r down
        
        l = 0
        r = len(height)-1 
        maxHeight = 0

        while l < r:
            h = min(height[l], height[r]) * (r-l)
            maxHeight = max(h, maxHeight)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxHeight
