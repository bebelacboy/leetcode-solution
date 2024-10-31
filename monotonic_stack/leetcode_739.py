from typing import List

class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack = []
    answer = [0 for _ in range(len(temperatures))]
    for i in range(len(temperatures)):
      if len(stack) == 0 or temperatures[i] < temperatures[stack[len(stack) - 1]]:
        stack.append(i)
        continue
      while len(stack) != 0 and temperatures[i] > temperatures[stack[len(stack) - 1]]:
        idx = stack.pop()
        answer[idx] = i - idx
      stack.append(i)
    return answer

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))