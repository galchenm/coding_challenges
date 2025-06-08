"""
This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
"""

from collections import defaultdict
def find_itinerary(flights, start):
    graph = defaultdict(list)
    
    # Build the graph
    for origin, destination in sorted(flights):
        graph[origin].append(destination)
    
    itinerary = []
    
    def visit(airport):
        while graph[airport]:
            next_airport = graph[airport].pop(0)
            visit(next_airport)
        itinerary.append(airport)
    
    visit(start)
    
    return itinerary[::-1] if len(itinerary) == len(flights) + 1 else None

# Example usage
if __name__ == "__main__":
    flights1 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
    start1 = 'YUL'
    print(find_itinerary(flights1, start1))  # Output: ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

    flights2 = [('SFO', 'COM'), ('COM', 'YYZ')]
    start2 = 'COM'
    print(find_itinerary(flights2, start2))  # Output: None

    flights3 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
    start3 = 'A'
    print(find_itinerary(flights3, start3))  # Output: ['A', 'B', 'C', 'A', 'C']