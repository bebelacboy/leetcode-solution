from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    merged = []
    intervals.sort(key=lambda e: e[0])
    for i in range(len(intervals)):
      if not merged or merged[-1][1] < intervals[i][0]:
        merged.append(intervals[i])
      else:
        merged[-1] = [merged[-1][0], max(merged[-1][1], intervals[i][1])]
    return merged
  
print(Solution().merge([[1,4],[0,2],[3,5]]))
    