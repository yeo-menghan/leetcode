# O(N^3) Time Limit Exceeded
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        # look left and right of the character
        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # Brute force
        for i in range(n):
            for j in range(i, n):
                # If substring from i to j is palindrome
                # increment the result
                if isPalindrome(s, i, j):
                    count += 1

        return count

# O(N^2) Expand around center with O(1) space
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expandAroundCenter(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            # single centers
            expandAroundCenter(i, i)
            # double centers
            expandAroundCenter(i, i+1)

        return count


# TODO: Classic DP Solution
