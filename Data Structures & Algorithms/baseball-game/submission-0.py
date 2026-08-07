class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for ch in operations:
            if ch =='+':
                record.append(record[-1] + record[-2])
            elif ch == 'C':
                record.pop()
            elif ch == 'D':
                record.append(2*record[-1])
            else:
               record.append(int(ch))          
        return sum(record)  
