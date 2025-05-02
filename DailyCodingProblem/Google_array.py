"""
This problem was recently asked by Google.

Given a list of numbers and a number k, 
return whether any two numbers from the list
add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.
"""

def has_pair_with_sum_two_pointers(numbers, k):
    left = 0
    right = len(numbers) - 1
    numbers.sort()
    while left <= right:
        curr = numbers[left] + numbers[right]
        if curr == k:
            return True
        elif curr < k:
            left += 1
        else:
            right -= 1
    return False

def has_pair_with_sum_hash_set(numbers, k):
    seen = set()
    for n in numbers:
        if k - n in numbers:
            return True
        seen.add(n)
    return False

def has_pair_with_sum_brute_force(numbers, k):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == k:
                return True
    return False

def time_evaluation(func, numbers, k):
    import time
    start_time = time.time()
    result = func(numbers, k)
    end_time = time.time()
    print(f"Name of the method {func.__name__} Result: {result}, Time taken: {end_time - start_time:.6f} seconds")
    
    
    numbers = [10, 15, 3, 7] * 1000  # Increase size for performance testing
    k = 1700
    start_time = time.time()
    result = func(numbers, k)
    end_time = time.time()
    print(f"Name of the method {func.__name__} Result: {result}, Time taken for larger input: {end_time - start_time:.6f} seconds")
    
if __name__ == "__main__":
    numbers = [10, 15, 3, 7]
    k = 17
    print("Using two pointers:")
    time_evaluation(has_pair_with_sum_two_pointers, numbers, k)
    
    print("Using hash set:")
    time_evaluation(has_pair_with_sum_hash_set, numbers, k)
    
    print("Using brute force:")
    time_evaluation(has_pair_with_sum_brute_force, numbers, k)