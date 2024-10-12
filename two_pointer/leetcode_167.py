from typing import List

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    x1 = 0
    x2 = len(numbers) - 1
    for i in range(len(numbers)):
      if numbers[x1] + numbers[x2] == target:
        return [x1 + 1, x2 + 1]
      elif numbers[x1] + numbers[x2] > target:
        x2 -= 1
      else:
        x1 += 1
    return [-1, -1]