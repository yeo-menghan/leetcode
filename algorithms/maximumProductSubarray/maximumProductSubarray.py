# Min/Max Tracking
# Time Complexity: O(N)
# Space Complexity: O(1) - stores 2 variables (min, max) and result
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod # swap if num is negative to account for -ve * -ve

            max_prod = max(num, num * max_prod)
            min_prod = min(num, num * min_prod)

            result = max(result, max_prod)

        return result

# DP solution
# Time Complexity: O(N)
# Space Complexity: O(N) - Stores two arrays of size N and result
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = dp_min[0] = nums[0]
        result = nums[0]

        for i in range(1, n):
            dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
            result = max(result, dp_max[i])

        return result
