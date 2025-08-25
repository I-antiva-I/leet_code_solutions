# LeetCode #0088 | Merge Sorted Array | [EASY]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        index_m = m-1
        index_n = n-1
        end = m+n-1

        while index_n >= 0:
            if index_m >= 0 and nums1[index_m] > nums2[index_n]:
                nums1[end] = nums1[index_m]
                index_m -= 1
            else:
                nums1[end] = nums2[index_n]
                index_n -= 1

            end -= 1

