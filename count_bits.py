def count_bits(num):
    """
    problem: Counting Bits
    source: https://leetcode.com/problems/counting-bits/
    """
    ones = [0]
    while len(ones) <= num:
        ones.extend([i + 1 for i in ones])
    return ones[:num+1]
