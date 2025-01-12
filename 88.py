from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_1 = m - 1
        index_2 = n - 1
        index_merge = m + n - 1
        while index_2 >= 0:
            if index_1 < 0 or nums2[index_2] >= nums1[index_1]:
                nums1[index_merge] = nums2[index_2]
                index_2 -= 1
            else:
                nums1[index_merge] = nums1[index_1]
                index_1 -= 1
            index_merge -= 1

        print(nums1)