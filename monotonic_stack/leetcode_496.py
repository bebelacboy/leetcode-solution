from typing import List

class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nge_map = {}
    stack = []
    for num in nums2:
      if len(stack) == 0 or num < stack[len(stack) - 1]:
        stack.append(num)
        continue
      while len(stack) > 0 and num > stack[len(stack) - 1]:
        nge_map[stack.pop()] = num
      stack.append(num)
    while len(stack) > 0:
      nge_map[stack.pop()] = -1
    for i in range(len(nums1)):
      nums1[i] = nge_map[nums1[i]]       
    return nums1

print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))