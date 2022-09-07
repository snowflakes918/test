
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums1.extend(nums2)
    nums1 = sorted(nums1)
    if len(nums1)%2 == 1:
        index = (len(nums1)-1)/2 + 1
        mid = nums1[int(index-1)]
        return mid
    elif len(nums1)%2 == 0:
        index1 = len(nums1)/2
        index2 = index1 + 1
        num1 = nums1[int(index1-1)]
        num2 = nums1[int(index2-1)]
        mid = (num1+num2)/2
        return mid

mid = findMedianSortedArrays([1, 2], [3, 4])
print(mid)