from typing import List

class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    maxSum = sum(nums[:k])
    eachSum = maxSum
    for i in range(1, len(nums) - k + 1):
      eachSum -= nums[i - 1] - nums[i + k - 1]
      maxSum = max(maxSum, eachSum)
    return float(maxSum) / k
  
print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))