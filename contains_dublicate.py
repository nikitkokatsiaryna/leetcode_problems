# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        index = 0

        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                return 'true'
            else:
                index += 1


solution = Solution()
solution_result = solution.containsDuplicate([3, 3, 7, 7, 10, 11, 11]) # true
# solution_result = solution.containsDuplicate([2, 14, 18, 22, 23])
print(solution_result)
