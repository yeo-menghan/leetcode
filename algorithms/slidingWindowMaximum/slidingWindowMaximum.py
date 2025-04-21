class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque() # stores indices in a monotonic deque
        result = []

        for i, num in enumerate(nums):
            # remove indices out of the window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove all elements smaller than the current from the back
            while deq and nums[deq[-1]] < num:
                deq.pop()

            deq.append(i)

            # the first element in deque is the max in the current window
            # can only start recording maximums after the first window is full
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result
