def rob(nums):
    """
    problem: House Robber
    source: https://leetcode.com/problems/house-robber/

    """
    p1 = p2 = max_money = 0
    for num in nums:
        max_money = p2 if p2 > p1 + num else p1 + num
        p1, p2 = p2, max_money
    return max_money
