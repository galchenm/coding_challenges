"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?


"""

def recursive_largest_sum(arr, i):
    if i >= len(arr):
        return 0
    if i == len(arr) - 1:
        return arr[i]
    return max(arr[i] + recursive_largest_sum(arr, i + 2), recursive_largest_sum(arr, i + 1))

def cached_largest_sum(arr, i, memo):
    if i >= len(arr):
        return 0
    if i in memo:
        return memo[i]
    if i == len(arr) - 1:
        return arr[i]
    memo[i] = max(arr[i] + cached_largest_sum(arr, i + 2, memo), cached_largest_sum(arr, i + 1, memo))
    return memo[i]

def constant_space_largest_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    prev = arr[0]
    curr = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        prev, curr = curr, max(curr, prev + arr[i])
    return curr