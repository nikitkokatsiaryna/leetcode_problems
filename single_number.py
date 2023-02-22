from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        return 2 * sum(set(nums)) - sum(nums)


solution = Solution()
print(solution.singleNumber([4, 1, 2, 1, 2]))  # 4
# print(solution.singleNumber([1]))   # 1
# print(solution.singleNumber([2, 2, 1]))  # 1
