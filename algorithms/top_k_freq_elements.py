from collections import defaultdict
import heapq


def top_k_frequent(nums, k):
    counter = defaultdict(int)
    for n in nums:
        counter[n] += 1
    return heapq.nlargest(k, counter, key=lambda x: counter[x])
