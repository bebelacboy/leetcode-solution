from typing import List

class NumArray:
  def __init__(self, nums: List[int]):
    self.nums = nums
    self.prefixsummed_nums = [nums[0]]
    for i in range(1, len(nums)):
      self.prefixsummed_nums.append(self.prefixsummed_nums[i - 1] + nums[i])

  def sumRange(self, left: int, right: int) -> int:
    if (left - 1 < 0):
      return self.prefixsummed_nums[right]
    return self.prefixsummed_nums[right] - self.prefixsummed_nums[left - 1]