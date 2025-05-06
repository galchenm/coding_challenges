"""
Convert a number to a binary coded decimal (BCD).

You can assume input will always be an integer. If it is a negative number then simply place a minus sign in front of the output string. Output will be a string with each digit of the input represented as 4 bits (0 padded) with a space between each set of 4 bits.

Ex.

n =  10 -> "0001 0000"
n = -10 -> "-0001 0000"
"""

def to_bcd(n):
    bcd_str = ""
    for digit in str(n):
        print(digit)
        if digit == "-":
             bcd_str += digit
             continue
        binary_digit = int(bin(int(digit))[2:])
        bcd_str += "{:04}".format(binary_digit) + " "
    return bcd_str.strip()
        

def to_bcd(n):
    return '-'*(n<0) + ' '.join(f'{int(d):0>4b}' for d in str(abs(n)))
