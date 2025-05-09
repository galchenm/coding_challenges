"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            hash_map[key].append(s)
        return list(hash_map.values())

"""
Example 2: 2260. Minimum Consecutive Cards to Pick Up

Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate.
If the array has no duplicates, return -1.
"""

from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(len(cards)):
            dic[cards[i]].append(i)
            
        ans = float("inf")
        for key in dic:
            arr = dic[key]
            for i in range(len(arr) - 1):
                ans = min(ans, arr[i + 1] - arr[i] + 1)
        
        return ans if ans < float("inf") else -1
    
from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = defaultdict(int)
        ans = float("inf")
        for i in range(len(cards)):
            if cards[i] in dic:
                ans = min(ans, i - dic[cards[i]] + 1)
            
            dic[cards[i]] = i

        return ans if ans < float("inf") else -1
    
    class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        freq = {}
        min_cards = float("inf")
        prev = 0

        for r in range(len(cards)):
            if cards[r] in freq:
                prev = freq[cards[r]]
                min_cards = min(min_cards, r - prev + 1)
            
            freq[cards[r]] = r
        
        return min_cards if min_cards != float("inf") else -1

"""
2342. Max Sum of a Pair With Equal Sum of Digits

Given an array of integers nums, find the maximum value of nums[i] + nums[j], where nums[i] and nums[j] have the same digit sum (the sum of their individual digits). 
Return -1 if there is no pair of numbers with the same digit sum.
"""

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_map = defaultdict(list)

        for n in nums:
            max_map[sum(map(int, str(n)))].append(n)
        
        max_value = min(nums)
        for s, numbers in max_map.items():
            if len(numbers)>1:
                numbers.sort(reverse = True)
                curr = sum(numbers[:2])
                max_value = max(max_value, curr)
        return max_value if max_value!= min(nums) else -1

from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            
            return digit_sum
        
        dic = defaultdict(int)
        ans = -1
        for num in nums:
            digit_sum = get_digit_sum(num)
            if digit_sum in dic:
                ans = max(ans, num + dic[digit_sum])
            dic[digit_sum] = max(dic[digit_sum], num)

        return ans

"""
2352. Equal Row and Column Pairs

Given an n x n matrix grid, return the number of pairs (R, C) 
where R is a row and C is a column, and R and C are equal 
if we consider them as 1D arrays.
"""
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = 0
        row_counts = defaultdict(int)
        for row in grid:
            row_counts[tuple(row)] += 1

        for column in zip(*grid):
            c += row_counts[column]

        return c