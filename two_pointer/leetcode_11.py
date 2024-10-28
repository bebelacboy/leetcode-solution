from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    result = 0
    x = 0
    i = 0
    j = len(height) - 1
    while x < len(height):
      if height[i] >= height[j]:
        result = max(result, height[j] * (j - i))
        j -= 1
      else:
        result = max(result, height[i] * (j - i))
        i += 1
      x += 1
    return result

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))