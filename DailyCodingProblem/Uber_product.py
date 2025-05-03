"""
This problem was asked by Uber.

Given an array of integers, return
a new array such that each element 
at index i of the new array is the 
product of all the numbers in the 
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output 
would be [2, 3, 6].
"""
import numpy as np

def product_array(arr):
    n = len(arr)
    if n == 0:
        return []
    total_product = np.prod(arr)
    return [total_product // arr[i] for i in range(n)]


def product_array_no_division(arr):
    n = len(arr)
    if n == 0:
        return []
    
    left_products = [1] * n
    right_products = [1] * n
    
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * arr[i - 1]
    
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * arr[i + 1]
    
    return [left_products[i] * right_products[i] for i in range(n)]

def time_evaluation(func, arr):
    import time
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    print(f"Name of the method {func.__name__} Time taken: {end_time - start_time:.6f} seconds")
    
    arr = [1, 2, 3, 4, 5] * 1000  # Increase size for performance testing
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    print(f"Name of the method {func.__name__} Time taken for larger input: {end_time - start_time:.6f} seconds")
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Using division:")
    time_evaluation(product_array, arr)
    
    print("\nUsing no division:")
    time_evaluation(product_array_no_division, arr)
    
    print("Using division:")
    time_evaluation(product_array, arr)
    
    