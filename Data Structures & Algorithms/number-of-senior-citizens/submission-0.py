class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for ch in details:
            if int(ch[11:13]) > 60:
                count += 1
        return  count       