class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxii = 0
        for i in range(len(s)):
            count = 0
            for j in range(i+1,len(s)+1):
                subs = s[i:j]
                if len(subs) == len(set(subs)):
                 count +=1 
                 maxii = max(count,maxii)
        return maxii        