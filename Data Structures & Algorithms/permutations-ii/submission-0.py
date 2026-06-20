class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        op = []
        nums.sort()
        def backtrack(cur,rem):
            if len(rem) == 0:
                op.append(cur)
                return

            for i in range(len(rem)):

                if i > 0 and rem[i] == rem[i-1]:
                    continue
                new_cur = cur + [rem[i]]
                new_rem = rem[:i] + rem[i+1:]
                backtrack(new_cur,new_rem)
        backtrack([],nums)
        return op        