from typing import List

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    prefix_sum = 0
    m = {0: 1}
    result = 0
    for i in range(len(nums)):
      prefix_sum += nums[i]
      if prefix_sum - k in m:
        result += m[prefix_sum-k]
      if prefix_sum not in m:
        m[prefix_sum] = 1
      else:
        m[prefix_sum] += 1
    return result