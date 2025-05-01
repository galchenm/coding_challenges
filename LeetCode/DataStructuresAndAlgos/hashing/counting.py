"""
Example 1: You are given a string s and an integer k. 
Find the length of the longest substring that contains at most k distinct characters.

For example, given s = 'eceba' and k = 2, return 3. 
The longest substring with at most 2 distinct characters is "ece".
"""
    
from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

"""
Example 2: 2248. Intersection of Multiple Arrays

Given a 2D array nums that contains n arrays of distinct integers, 
return a sorted array containing all the numbers that appear in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4].
3 and 4 are the only numbers that are in all arrays.
"""
from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)
        
        return sorted(ans)
    

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        acc = set(nums[0])

        for i in range(1, len(nums)):
            acc = acc.intersection(nums[i])

        return sorted(list(acc))
    
"""
Example 3: 1941. Check if All Characters Have Equal Number of Occurrences

Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true. All characters appear twice.
Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
"""

from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        frequencies = counts.values()
        return len(set(frequencies)) == 1
    
from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = {char: s.count(char) for char in set(s)}
        values = list(count.values())
        return all(v == values[0] for v in values)

from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s)
        return len(set(freq.values())) == 1

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        tung_chu = set(s)
        first_count = s.count(list(tung_chu)[0])
        for i in tung_chu:
            if s.count(i) != first_count:
                return False
        return True
    
"""
Example 4: 560. Subarray Sum Equals K

Given an integer array nums and an integer k, find 
the number of subarrays whose sum is equal to k.
"""

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        We use curr to track the prefix sum.
        At any index i, the sum up to i is curr. If there is an index j whose prefix is curr - k, then the sum of the subarray with elements from j + 1 to i is curr - (curr - k) = k.
        Because the array can have negative numbers, the same prefix can occur multiple times. We use a hash map counts to track how many times a prefix has occurred.
        At every index i, the frequency of curr - k is equal to the number of subarrays whose sum is equal to k that end at i. Add it to the answer.
        """
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
    
        return ans
    
"""
Example 5: 1248. Count Number of Nice Subarrays

Given an array of positive integers nums and an integer k. 
Find the number of subarrays with exactly k odd numbers in them.

For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. 
The subarrays with 3 odd numbers in them are [1, 1, 2, 1, 1] and [1, 1, 2, 1, 1].
"""

from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        
        for num in nums:
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans