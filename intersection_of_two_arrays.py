# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from typing import List


class Solution:

    def get_intersect(self, main_nums, intersect_nums):
        intersaction = []

        for el in main_nums:
            if el in intersect_nums:
                intersaction.append(el)
                intersect_nums[intersect_nums.index(el)] = '-'
        return intersaction

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) < len(nums2):
            return self.get_intersect(nums1, nums2)
        elif len(nums1) > len(nums2):
            return self.get_intersect(nums2, nums1)
        else:
            return self.get_intersect(nums1, nums2)


solution = Solution()
print(solution.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))  # [4,9]
# print(solution.intersect(nums1=[1, 2], nums2=[1, 1]))  # [1]
# print(solution.intersect(nums1=[3, 1, 2], nums2=[1, 1]))  # [1]
# print(solution.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))  # [2,2]
