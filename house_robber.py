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


def rob2(nums):
    """
    problem: House Robber II
    source: https://leetcode.com/problems/house-robber-ii/

    """
    size = len(nums)
    if size == 1:
        return nums[0]
    m1 = rob(nums[1:])
    m2 = rob(nums[:-1])
    return m1 if m1 > m2 else m2
