class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using counting sort
        count0 = count1 = count2 = 0

        # count frequency
        for num in nums:
            if num == 0:
                count0+=1
            elif num == 1:
                count1+=1
            elif num == 2:
                count2+=1

        # overwrite array
        idx = 0
        for _ in range(count0):
            nums[idx] = 0
            idx += 1
        for _ in range(count1):
            nums[idx] = 1
            idx += 1
        for _ in range(count2):
            nums[idx] = 2
            idx += 1
