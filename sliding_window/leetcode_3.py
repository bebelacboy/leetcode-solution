class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      charSet = {}
      if len(s) > 0: 
        charSet[s[0]] = 0
      else:
        return 0
      i = 0
      j = 1
      result = 0
      while j < len(s):
        if s[j] in charSet:
          result = max(j - i, result)
          while i <= charSet[s[j]]:
            if i == charSet[s[j]]:
              i += 1
              break
            del charSet[s[i]]
            i += 1
        charSet[s[j]] = j
        j += 1
      result = max(j - i, result)
      return result
print(Solution().lengthOfLongestSubstring("au"))