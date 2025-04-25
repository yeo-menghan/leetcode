# Monotonic Stack - O(N)
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        results = [0] * n
        stack = []
        for i in range (n-1, -1, -1):
            count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            if stack:
                count += 1 # the first taller / equal person
            results[i] = count
            stack.append(heights[i])

        return results
