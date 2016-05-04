def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums = [(n, i) for i, n in enumerate(nums)]
    nums.sort()
    front = 0
    rear = len(nums) - 1
    while front < rear:
        if nums[front][0] + nums[rear][0] < target:
            front += 1
        elif nums[front][0] + nums[rear][0] > target:
            rear -= 1
        else:
            return [nums[front][1], nums[rear][1]]
