from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # for num in nums:
        #     res += [box + [num] for box in res]
        # return res    
        for i in range(len(nums)+1):
            for item in combinations(nums,i):
                res.append(list(item))
        return res        