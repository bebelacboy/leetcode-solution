from typing import List

class Solution:
    def pop(self, heap):
      if len(heap) == 1:
        heap.pop()
        return heap
      heap[0] = heap.pop()
      idx = 0
      temp = 0
      child_idx = 0
      if len(heap) > idx * 2 + 2:
        child_idx = idx * 2 + 1 if heap[idx * 2 + 2] >= heap[idx * 2 + 1] else idx * 2 + 2
      elif len(heap) > idx * 2 + 1:
        child_idx = idx * 2 + 1
      while idx < len(heap) - 1 and heap[child_idx] < heap[idx]:
        temp = heap[child_idx]
        heap[child_idx] = heap[idx]
        heap[idx] = temp
        idx = child_idx
        if len(heap) > idx * 2 + 2:
          child_idx = idx * 2 + 1 if heap[idx * 2 + 2] >= heap[idx * 2 + 1] else idx * 2 + 2
        elif len(heap) > idx * 2 + 1:
          child_idx = idx * 2 + 1
      return heap
    def push(self, heap, num):
      heap.append(num)
      idx = len(heap) - 1
      temp = 0
      while idx > 0 and heap[idx] < heap[(idx - 1) // 2]:
        temp = heap[(idx - 1) // 2]
        heap[(idx-1) // 2] = heap[idx]
        heap[idx] = temp
        idx = (idx-1) // 2
      return heap
      
    def findKthLargest(self, nums: List[int], k: int) -> int:
      heap = []
      for i in range(k):
        heap = self.push(heap, nums[i])
      nums = nums[k:]
      for num in nums:
        if num > heap[0]:
          heap = self.pop(heap)
          heap = self.push(heap, num)
      return heap[0]

print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 20))