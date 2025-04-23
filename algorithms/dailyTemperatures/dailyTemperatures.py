# Stack Solution - O(N)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n
        stack = [] # store indices, contains indices of days waiting for a warmer day
        for i, temp in enumerate(temperatures): #i: current day (index), temp: current day's temperature
            while stack and temp > temperatures[stack[-1]]:
                # current temp warmer than day at top of the stack ==> current day is the next warmer day for prev_index's day
                prev_index = stack.pop()
                results[prev_index] = i - prev_index
            stack.append(i) # push current day's index into stack
        return results

# Jump Pointer approach - O(N)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n
        for i in range(n - 2, -1, -1):  # Start from second last element, top at index 0 and decrement by 1 / step
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if results[j] == 0:
                    j = n  # No warmer day ahead
                else:
                    j += results[j]  # Jump ahead by the number of days to the next warmer temp
            if j < n:
                results[i] = j - i
        return results
