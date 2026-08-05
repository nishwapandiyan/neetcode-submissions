from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []
        for i in range(len(nums)+1):
            for v in combinations(nums,i):
                lst.append(v)
        return list(set(lst))