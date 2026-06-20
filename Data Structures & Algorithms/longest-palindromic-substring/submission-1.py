class Solution:
    def longestPalindrome(self, s: str) -> str:

        w = {}
        cur = 0
        prev = 0
        res = ""
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                cur = len(sub)
                if sub == sub[::-1]:
                    w[sub] = cur
                    if cur > prev:
                        res = sub
                        prev = cur


    
        return res
