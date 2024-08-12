class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = 0

        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            most_water = max(most_water, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return most_water
