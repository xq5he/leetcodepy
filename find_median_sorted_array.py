def find_kth(nums1, nums2, k):
    if not nums1:
        return nums2[k]
    if not nums2:
        return nums1[k]
    if k == 0:
        return min(nums1[0], nums2[0])
    half_idx = (k - 1)/2 if k % 2 == 0 else k/2
    idx1 = half_idx if half_idx < len(nums1) else len(nums1) - 1
    idx2 = half_idx if half_idx < len(nums2) else len(nums2) - 1
    if nums1[idx1] < nums2[idx2]:
        return find_kth(nums1[idx1 + 1:], nums2, k - idx1 - 1)
    else:
        return find_kth(nums1, nums2[idx2 + 1:], k - idx2 - 1)


def find_median(nums1, nums2):
    l = len(nums1) + len(nums2)
    if l % 2 == 1:
        return find_kth(nums1, nums2, (l - 1) / 2)
    else:
        return (
            find_kth(nums1, nums2, (l - 1) / 2) +
            find_kth(nums1, nums2, (l + 1) / 2)
        ) / 2.0
