from typing import List

class Solution:
  def findMaxLength(self, nums: List[int]) -> int:
    n1 = 0
    m = {}
    m[0] = -1
    max_len = 0
    
    for i in range(len(nums)):
      n1 += nums[i]
      n0 = i + 1 - n1
      if ((n1-n0) not in m):
        m[n1-n0] = i
      else:
        max_len = max(max_len, i - m[n1-n0])
    return max_len