# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    head = None
    cursor = None
    carry = False
    while l1 or l2:
        l1_val = l1.val if l1 else 0
        l1 = l1.next if l1 else None
        l2_val = l2.val if l2 else 0
        l2 = l2.next if l2 else None
        _sum = l1_val + l2_val + (1 if carry else 0)
        carry = _sum >= 10
        next_node = ListNode(_sum % 10)
        if cursor:
            cursor.next = next_node
        else:
            cursor = next_node
            head = cursor
        cursor = next_node
    if carry:
        cursor.next = ListNode(1)
    return head
