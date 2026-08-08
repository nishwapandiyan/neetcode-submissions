class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        maxx = nums[0]
        cur = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cur += nums[i]
            else:
                cur = nums[i]
            maxx = max(maxx,cur)
        return maxx            