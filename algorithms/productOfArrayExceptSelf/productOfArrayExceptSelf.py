class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Prefix Pass: For each index, store the product of all numbers to its left.
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Suffix Pass: For each index, multiply by the product of all numbers to its right.
        suffix = 1
        for i in range(n - 1, -1, -1): # start at n-1, stop at index 0, decrement by 1 each loop (count backwards)
            result[i] *= suffix  # Multiply with the current suffix product
            suffix *= nums[i]  # Update the suffix product

        return result
