def is_palindrome(s):
    return s == s[::-1]


def get_palindrome_pairs(words):
    indices = set()
    reversed_words = {word[::-1]: i for i, word in enumerate(words)}
    for j, word in enumerate(words):
        for i in range(0, len(word) + 1):
            left = word[:i]
            reversed_left = left[::-1]
            left_index = reversed_words.get(left)
            if (left_index is not None and
                    j != left_index and
                    is_palindrome(word + reversed_left)):
                indices.add((j, left_index))

            right = word[i:]
            reversed_right = right[::-1]
            right_index = reversed_words.get(right)
            if (right_index is not None and
                    j != right_index and
                    is_palindrome(reversed_right + word)):
                indices.add((right_index, j))

    return list(indices)
