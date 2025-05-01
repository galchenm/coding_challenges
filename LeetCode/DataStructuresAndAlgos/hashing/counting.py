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
    
