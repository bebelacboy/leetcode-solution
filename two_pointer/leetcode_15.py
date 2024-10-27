from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    i = 0
    j = 1
    k = len(nums) - 1
    result = []
    while i < len(nums) - 2:
      if i > 0 and nums[i] == nums[i  - 1]:
        i += 1
        j = i + 1
        k = len(nums) - 1 
        continue
      while (j < k):
        if k < len(nums) - 1 and nums[k] == nums[k + 1]:
          k -= 1
          continue
        if j > i + 1 and nums[j] == nums[j - 1]:
          j += 1
          continue
        if nums[i] + nums[j] + nums[k] == 0:
          result.append([nums[i], nums[j], nums[k]])
          k -= 1
        elif nums[i] + nums[j] + nums[k] > 0:
          k -= 1
        else:
          j += 1
      i += 1
      j = i + 1
      k = len(nums) - 1

    return result
        
        
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))