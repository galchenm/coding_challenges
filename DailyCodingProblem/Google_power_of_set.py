"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

def power_set(s):
    result = [[]]  # Start with the empty set
    for elem in s:
        # For each element, add it to all existing subsets
        result += [curr + [elem] for curr in result]
    return result


# Example usage
if __name__ == "__main__":
    s = [1, 2, 3]
    print(power_set(s))  # Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]