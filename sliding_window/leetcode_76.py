from collections import defaultdict


class Solution:
  def minWindow(self, s: str, t: str) -> str:
    ch_counts = defaultdict(int)
    for x in t:
      ch_counts[x] += 1
    start = 0
    end = 0
    remaining_char = len(t)
    min_window = None
    while end < len(s):
      if ch_counts[s[end]] > 0:
        remaining_char -= 1
      ch_counts[s[end]] -= 1
      if remaining_char == 0:
        while start <= end:
          if ch_counts[s[start]] >= 0:
            if remaining_char == 0:
              if not min_window or end - start < min_window[1] - min_window[0]:
                min_window = (start, end)
              
            elif remaining_char == 1:
              break
            remaining_char += 1
          ch_counts[s[start]] += 1
          start += 1
      end += 1
    return "" if not min_window else  s[min_window[0]:min_window[1] + 1]
      

print(Solution().minWindow("aaflslflsldkalskaaa", "aaa"))