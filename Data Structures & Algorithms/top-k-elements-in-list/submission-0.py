from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p = Counter(nums)
        return [num for num,_ in p.most_common(k)]