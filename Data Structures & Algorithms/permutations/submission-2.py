class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        op = []

        def backtrack(cur,rem):

            if len(rem) == 0:
                op.append(cur)
            for i in range(len(rem)):
                new_cur = cur + [rem[i]]
                new_rem = rem[:i] + rem[i+1:]
                backtrack(new_cur,new_rem)
        backtrack([],nums)
        return op        

        