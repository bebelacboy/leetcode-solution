from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    inserted = False
    i = 0
    if (newInterval[1] < intervals[i][0] or newInterval[0] > intervals[i][1]):
      inserted = True
      result.append(newInterval)
    while i < len(intervals):
      if newInterval[1] >= intervals[i][0] and newInterval[0] <= intervals[i][1]:
        newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
      elif newInterval[0] < intervals[i][0] and not inserted:
        inserted = True
        result.append(newInterval)
        result.append(intervals[i])
      else:
        result.append(intervals[i])
      i += 1  
    if len(result) == 0 or not inserted:
      result.append(newInterval)
    return result
            
  
print(Solution().insert([[3,5], [12,15]], [6,6]))