class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = [x for x in nums1 if x in nums2]
        return list(set(lst)) 