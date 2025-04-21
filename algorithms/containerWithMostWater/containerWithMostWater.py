# 2-pointer approach

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left) # min height * width separating pointers
            max_area = max(max_area, area)

            # move the pointer of the lower height inwards
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
