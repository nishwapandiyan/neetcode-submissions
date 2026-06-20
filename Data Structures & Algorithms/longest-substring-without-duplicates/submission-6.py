class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        lst = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if len(s[i:j]) == len(list(set(s[i:j]))):
                  lst.append(len(s[i:j]))
        return max(lst)