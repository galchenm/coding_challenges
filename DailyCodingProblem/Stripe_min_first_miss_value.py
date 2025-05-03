"""
This problem was asked by Stripe.

Given an array of integers, find the 
first missing positive integer in linear 
time and constant space. In other words, 
find the lowest positive integer that does not 
exist in the array. The array can contain duplicates 
and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. 
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def first_missing_positive(nums):
    n = len(nums)
    
    # Step 1: Replace negative numbers and zeros with n+1
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1
    
    # Step 2: Use the index as a hash to mark the presence of numbers
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    
    return next((i + 1 for i in range(n) if nums[i] > 0), n + 1)

def first_missing_positive_another_approach(nums):
    seen = set()
    for n in nums:
        if n > 0:
            seen.add(n)
    seen = sorted(seen)
    for i in range(1, len(seen) + 1):
        if i not in seen:
            return i
    return len(seen) + 1

def time_evaluation(func, nums):
    import time
    start_time = time.time()
    result = func(nums)
    end_time = time.time()
    print(f"Name of the method {func.__name__} Result: {result}, Time taken: {end_time - start_time:.6f} seconds")
    
    nums = [3, 4, -1, 1] * 1000  # Increase size for performance testing
    start_time = time.time()
    result = func(nums)
    end_time = time.time()
    print(f"Name of the method {func.__name__} Result: {result}, Time taken for larger input: {end_time - start_time:.6f} seconds")
    
    
    
if __name__ == "__main__":
    nums = [3, 4, -1, 1]
    print("Using first_missing_positive:")
    time_evaluation(first_missing_positive, nums)
    
    time_evaluation(first_missing_positive_another_approach, nums)
    nums = [1, 2, 0]
    print("Using first_missing_positive:")
    time_evaluation(first_missing_positive, nums)
    time_evaluation(first_missing_positive_another_approach, nums)
    nums = [1, 2, 3]
    print("Using first_missing_positive:")
    time_evaluation(first_missing_positive, nums)
    time_evaluation(first_missing_positive_another_approach, nums)
    
    nums = [0, 0, 0]
    print("Using first_missing_positive:")
    time_evaluation(first_missing_positive, nums)
    time_evaluation(first_missing_positive_another_approach, nums)
    
    nums = [1, 2, 3, 4, 5]
    print("Using first_missing_positive:")
    time_evaluation(first_missing_positive, nums)
    time_evaluation(first_missing_positive_another_approach, nums)
    
    nums = [1, 2, 3, 4, 5] * 1000  # Increase size for performance testing
    print("Using first_missing_positive:")
    time_evaluation(first_missing_positive, nums)
    time_evaluation(first_missing_positive_another_approach, nums)
    