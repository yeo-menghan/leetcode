class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for item in nums:
            if item in seen:
                return True
            else:
                seen.add(item)

        return False
