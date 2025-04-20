class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane’s Algorithm
        # max_current: the best sum ending at the current position
        # max_global: the best sum found so far anywhere
        max_current = max_global = nums[0]

        for num in nums[1:]:
            max_current = max(num, num + max_current) # num => start new subarray, num + max_current => continue subarray
            if max_current > max_global:
                max_global = max_current

        return max_global
