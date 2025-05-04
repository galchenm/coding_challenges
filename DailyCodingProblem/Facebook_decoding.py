"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, 
and an encoded message, count the number of 
ways it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable.
For example, '001' is not allowed.
"""

def count_decodings(message):
    if not message or message[0] == '0':
        return 0

    n = len(message)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        if message[i - 1] != '0':
            dp[i] += dp[i - 1]
        if 10 <= int(message[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

if __name__ == "__main__":
    message = "111"
    print(f"Number of ways to decode '{message}': {count_decodings(message)}")
    # Test case to check if the decoded message matches the expected output
    assert count_decodings(message) == 3, "Test case failed!"
    print("Test case passed!")