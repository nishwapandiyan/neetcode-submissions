class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        n = len(s)
        window = set()
        max_l = 0

        while j < n:

             while s[j] in window:
                 window.remove(s[i])
                 i += 1
             window.add(s[j])
     
             max_l = max(max_l, j-i+1)
             j += 1
        return max_l   