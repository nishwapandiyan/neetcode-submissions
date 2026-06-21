class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) #nums = [1,2,3]
        i = n -2  #1
        while i >= 0 and nums[i] >= nums[i+1]: # 2 > 3
              i -= 1
        if i>=0:
            j = n-1
            while nums[j] <= nums[i]:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
        l= i+1
        r = n-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        return nums            