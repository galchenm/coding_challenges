"""
This problem was asked by Amazon.

Given an integer k and a string s, 
find the length of the longest substring
that contains at most k distinct 
characters.

For example, given 
s = "abcba" and k = 2, the longest 
substring with k distinct characters
is "bcb".
"""

from collections import defaultdict
def longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0
    
    left = 0
    char_count = defaultdict(int)
    max_length = 0
    for right in range(len(s)):
        char_count[s[right]] += 1
        while len(char_count)>k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

# Example usage
if __name__ == "__main__":
    s = "abcba"
    k = 2
    print(longest_substring_k_distinct(s, k))  # Output: 3
        