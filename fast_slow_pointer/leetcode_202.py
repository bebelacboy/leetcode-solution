class Solution:
  def isHappy(self, n: int) -> bool:
    sum_of_square = sum([int(x)**2 for x in str(n)])
    seen = set()
    while sum_of_square not in seen:
      if sum_of_square == 1:
        return True
      seen.add(sum_of_square)
      sum_of_square = sum([int(x)**2 for x in str(sum_of_square)])
    return False