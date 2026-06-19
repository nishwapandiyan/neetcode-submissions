class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        cur = 0
        for ch in nums:
            if ch != 1:
                cur = 0
            else:
                cur += 1
            count = max(count,cur)    
        return count            