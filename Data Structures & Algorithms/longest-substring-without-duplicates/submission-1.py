from itertools import combinations
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # maxii = 0
        # for i in range(len(s)):
        #     count = 0
        #     for j in range(i+1,len(s)+1):
        #         subs = s[i:j]
        #         if len(subs) == len(set(subs)):
        #          count +=1 
        #          maxii = max(count,maxii)
        # return maxii       

        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
