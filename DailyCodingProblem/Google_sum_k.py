"""
This problem was asked by Google.

Given a list of integers S and a target number k, 
write a function that returns a subset of S that adds up to k. 
If such a subset cannot be made, then return null.

Integers can appear more than once in the list. 
You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, 
return [12, 9, 2, 1] since it sums up to 24.
"""

def find_subset_with_sum(S, k):
    def backtrack(start, current_subset, current_sum):
        if current_sum == k:
            return current_subset
        if current_sum > k or start >= len(S):
            return None
        
        # Include the current element
        include = backtrack(start + 1, current_subset + [S[start]], current_sum + S[start])
        if include is not None:
            return include
        
        # Exclude the current element
        exclude = backtrack(start + 1, current_subset, current_sum)
        return exclude
    
    return backtrack(0, [], 0)

def another_find_subset_with_sum(S, k):
    n = len(S)
    dp = [None] * (k + 1)
    dp[0] = []
    
    for num in S:
        for j in range(k, num - 1, -1):
            if dp[j - num] is not None:
                dp[j] = dp[j - num] + [num]
    
    return dp[k]

def third_find_subset(s, k):
    s.sort()
    n = len(s)
    curr = 0
    result = []
    for i in range(n - 1, -1, -1):
        if curr + s[i] <= k:
            curr += s[i]
            result.append(s[i])
        if curr == k:
            return result
    return None
# Example usage
if __name__ == "__main__":
    S = [12, 1, 61, 5, 9, 2]
    k = 24
    subset = find_subset_with_sum(S, k)
    print("Subset with sum {}: {}".format(k, subset))
    
    another_subset = another_find_subset_with_sum(S, k)
    print("Another subset with sum {}: {}".format(k, another_subset))
    
    third_subset = third_find_subset(S, k)
    print("Third subset with sum {}: {}".format(k, third_subset))