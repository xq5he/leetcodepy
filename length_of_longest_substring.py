def length_of_longest_substring(s):
    front_idx = 0
    rear_idx = 0
    substring = ''
    max_length = 0
    for i, c in enumerate(s):
        if c not in substring:
            rear_idx += 1
            substring += c
        else:
            max_length = max(max_length, rear_idx - front_idx)
            appear_idx = front_idx + substring.find(c)
            front_idx = appear_idx + 1
            rear_idx = i + 1
            substring = s[front_idx:rear_idx]
    max_length = max(max_length, rear_idx - front_idx)
    return max_length
