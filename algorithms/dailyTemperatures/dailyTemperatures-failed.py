# Time limit exceeded on test case 36/48 - O(N^2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    results[i] = j - i
                    break

        return results
