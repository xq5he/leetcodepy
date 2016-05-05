def reverse_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s = list(s)
    front, rear = 0, len(s) - 1
    while front < rear:
        if s[front] not in vowels:
            front += 1
        if s[rear] not in vowels:
            rear -= 1
        if s[front] in vowels and s[rear] in vowels:
            s[front], s[rear] = s[rear], s[front]
            front += 1
            rear -= 1
    return ''.join(s)
