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


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def rob3(root):
    """
    problems: House Robber III
    source: https://leetcode.com/problems/house-robber-iii/
    """
    # global dict used to keep max money of a node which has been calculated
    memo = {}

    def _rob(root):
        if root is None:
            return 0
        # rob root
        left_gc = [root.left.left, root.left.right] if root.left else []
        right_gc = [root.right.left, root.right.right] if root.right else []
        grandchildren = left_gc + right_gc
        money_root = root.val
        for gc in grandchildren:
            memo[gc] = memo.get(gc) or _rob(gc)
            money_root += memo[gc]
        # do not rob root
        money_left = memo.get(root.left) or _rob(root.left)
        money_right = memo.get(root.right) or _rob(root.right)
        memo[root.left], memo[root.right] = money_left, money_right

        return max(money_root, money_left + money_right)
    return _rob(root)
