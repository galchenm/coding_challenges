"""
Summary
Given a Hash made up of keys and values, invert the hash by swapping them.

Examples
Given:

  { 'a' : 1,
    'b' : 2,
    'c' : 3 }

Return:

  { 1 : 'a',
    2 : 'b',
    3 : 'c' }
"""

def invert_hash(dictionary):
    return {value: key for key,value in dictionary.items()}

