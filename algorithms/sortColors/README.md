# Sort Colors - Dutch National Flag Algorithm

Single pass, in-place using 3 pointers

## Code

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else: # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

```

## Main Idea
The array is divided into four sections:

- `[0, low-1]`: All 0s (already sorted)
- `[low, mid-1]`: All 1s (already sorted)
- `[mid, high]`: Unsorted elements (to be examined)
- `[high+1, end]`: All 2s (already sorted)

The pointers are:
- `low`: Boundary between 0s and 1s
- `mid`: Current element being examined
- `high`: Boundary between 1s/unknown and 2s


## Algorithm Analysis
Why does this algorithm work?
- If arr[mid] == 0: swap to the front where 0s belong, expand both low and mid.
- If arr[mid] == 1: 1 already in the right place, just move mid ahead.
- If arr[mid] == 2: swap to the end where 2s belong, shrink high (but don't increment mid, since the swapped-in element at mid hasn't been checked yet).

Time Complexity (one-pass)
- Best Case: O(n)
- Worst Case: O(n)
- Average Case: O(n)

Space Complexity
- O(1) auxilliary space
- Sorting done in place, uses a constant number of helper variables

NOTE: not a stable sort; relative order of equal elements will not be preserved

Comparison to Counting Sort
- Counting sort also runs in O(n) time but uses O(k) space where k is the number of unique values
