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
solution_result = solution.containsDuplicate([3, 3, 7, 7, 10, 11, 11])
# solution_result = solution.containsDuplicate([2, 14, 18, 22, 23])
print(solution_result)
