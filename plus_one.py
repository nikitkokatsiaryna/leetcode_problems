from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        to_str = [str(num) for num in digits]
        joined_str = ''.join(to_str)
        result_int = int(joined_str) + 1

        return [int(el) for el in str(result_int)]


solution = Solution()
# print(solution.plusOne([1, 2, 3]))  # [1, 2, 4]
# print(solution.plusOne([4, 3, 2, 1]))  # [4,3,2,2]
print(solution.plusOne([9]))  # [1, 0]
# print(solution.plusOne([9, 9]))  # [1, 0, 0]
