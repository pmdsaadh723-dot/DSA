class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1 + nums2
        a.sort()
        n = len(a)
        if n % 2 == 1:
            return float(a[n // 2])
        else:
            return (a[n // 2 - 1] + a[n // 2]) / 2.0