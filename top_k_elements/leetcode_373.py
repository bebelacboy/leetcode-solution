from typing import List
import heapq

class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    heap = []
    res = []
    for i in range(min(len(nums1), k)):
      heapq.heappush(heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
    while k > 0 and len(heap) > 0:
      k -= 1
      popped = heapq.heappop(heap)
      res.append((popped[1], popped[2]))
      if popped[3] + 1 < len(nums2):
        heapq.heappush(heap, (popped[1] + nums2[popped[3] + 1], popped[1], nums2[popped[3] + 1], popped[3] + 1))
    return res
      
    
print(Solution().kSmallestPairs([1,7,11], [2,4,6], 3))
          