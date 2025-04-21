# Sliding Window Maximum

## Problem Statement

Given an array of integers `nums` and an integer `k`, find the maximum value in each sliding window of size `k` as it moves from left to right across the array.

**Example:**
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Each output element is the maximum of the window `[nums[i], nums[i+1], ..., nums[i+k-1]]`.


## Approach

### Naive Solution

For each window, iterate through the `k` elements and find the maximum.
- **Time Complexity:** O(nk)
- **Inefficient** for large arrays.

### Optimal Solution: [Monotonic Deque](https://www.geeksforgeeks.org/introduction-to-monotonic-queues/)

We use a **deque (double-ended queue)** to keep track of indices of elements that could be the maximum in the current window. The deque maintains a decreasing order of values. This allows us to always access the maximum in constant time and update the window efficiently.

**Key Steps:**
1. **Pop indices from the front** if they are out of the current window.
2. **Pop indices from the back** if their corresponding values are less than the current element's value.
3. **Append the current index** to the deque.
4. **Record the max** (the value at the front of the deque) when the first window is reached (`i >= k-1`).

**Complexity**
- **Time Complexity:** O(n)
- **Space Complexity:** O(k)
