class Solution:
    def longestPalindrome(self, s: str) -> str:

        w = {}
        cur = 0
        maxl = 0

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                cur = len(sub)
                if sub == sub[::-1]:
                    w[sub] = cur
        res = "" 
        prev = 0
        for key ,val in w.items():
            if val > prev:
                res = key
                prev = val
        return res
