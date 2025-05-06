"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

"""
    
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = defaultdict(int)

        for winner, loser in matches:
            # Make sure winner is recorded even if they never lost
            if winner not in loss_count:
                loss_count[winner] = 0
            loss_count[loser] += 1

        zero_losses = []
        one_loss = []

        for player in loss_count:
            if loss_count[player] == 0:
                zero_losses.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)

        return [sorted(zero_losses), sorted(one_loss)]


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        multipleLosses = set()
        allLoses = set()
        wins = set()

        for w, l in matches:
            if l in allLoses:
                multipleLosses.add(l)
            wins.add(w)
            allLoses.add(l)

        return [sorted(list(wins-allLoses)), sorted(list(allLoses-multipleLosses))]

"""
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

 

Example 1:

Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
Example 2:

Input: nums = [9,9,8,8]
Output: -1
Explanation: There is no number that occurs only once.
 

Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 1000
"""

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        keys = sorted(count.keys())
        ans = -1
        for k in keys:
            if count[k] == 1 and k > ans:
                ans = k
        return ans
    
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # If there's only one element, it's unique by default
        if n == 1:
            return nums[0]

        nums.sort(reverse=True)

        # Start from the beginning (largest numbers)
        currentIndex = 0

        while currentIndex < n:
            # If it's the first element or different from the next one, it's unique
            if (
                currentIndex == n - 1
                or nums[currentIndex] != nums[currentIndex + 1]
            ):
                return nums[currentIndex]
            # Skip duplicates
            while (
                currentIndex < n - 1
                and nums[currentIndex] == nums[currentIndex + 1]
            ):
                currentIndex += 1
            # Move to the next unique number
            currentIndex += 1

        return -1
    
    class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # Use Counter to count frequencies of numbers
        frequency_map = Counter(nums)

        # Find the largest number with frequency 1, or -1 if none found
        return max(
            (num for num, freq in frequency_map.items() if freq == 1),
            default=-1,
        )
        
"""

"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {ch: 0 for ch in "balloon"}
        
        for ch in text:
            if ch in count:
                count[ch] += 1

        # Since 'l' and 'o' appear twice in "balloon", we divide their counts by 2
        count['l'] //= 2
        count['o'] //= 2

        # The answer is the minimum count among all required characters
        return min(count[ch] for ch in "balon")

"""
"""

