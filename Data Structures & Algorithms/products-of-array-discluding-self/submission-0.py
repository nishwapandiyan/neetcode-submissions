class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            val = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    val *= nums[j]
            res[i] = val
        return res            