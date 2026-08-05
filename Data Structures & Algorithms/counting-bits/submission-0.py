class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            s = bin(i)
            lst.append(s.count('1'))
        return lst