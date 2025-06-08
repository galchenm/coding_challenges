"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""

import heapq
class RunningMedian:
    def __init__(self):
        self.lower_half = []  # Max heap (inverted min heap)
        self.upper_half = []  # Min heap

    def add_number(self, num):
        # Add to max heap (lower half)
        if not self.lower_half or num <= -self.lower_half[0]:
            heapq.heappush(self.lower_half, -num)
        else:
            heapq.heappush(self.upper_half, num)

        # Balance the heaps
        if len(self.lower_half) > len(self.upper_half) + 1:
            moved_value = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, moved_value)
        elif len(self.upper_half) > len(self.lower_half):
            moved_value = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -moved_value)

    def get_median(self):
        if len(self.lower_half) > len(self.upper_half):
            return -self.lower_half[0]
        return (-self.lower_half[0] + self.upper_half[0]) / 2.0
    
def running_median(sequence):
    median_calculator = RunningMedian()
    medians = []
    
    for num in sequence:
        median_calculator.add_number(num)
        medians.append(median_calculator.get_median())
    
    return medians

# Example usage
if __name__ == "__main__":
    sequence = [2, 1, 5, 7, 2, 0, 5]
    medians = running_median(sequence)
    for median in medians:
        print(median)