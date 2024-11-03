from typing import List
import heapq

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counter = {}
    result = []
    for num in nums:
      if num not in counter:
        counter[num] = 0
      else:
        counter[num] += 1
    nums_counts = [(value, key) for  key, value in counter.items()]
    heap = nums_counts[:k]
    nums_counts = nums_counts[k:]
    heapq.heapify(heap)
    for numcount in nums_counts:
      if numcount[0] > heap[0][0]:
        heapq.heapreplace(heap, numcount)
    while len(heap) > 0:
      result.append(heapq.heappop(heap)[1])
    return result
    
print(Solution().topKFrequent([1,1,1,2,2,3], 2))
    