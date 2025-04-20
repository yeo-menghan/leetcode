# O(N^2) implementation using 2 for loops
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if the two numbers sum to the target
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# O(N) using hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index] # if complement is found, return both indexes
            num_to_index[num] = index

        return []
