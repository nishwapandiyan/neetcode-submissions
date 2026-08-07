class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        lst = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j:
                    continue
                if words[i] in words[j]:
                    lst.append(words[i])
        return list(set(lst))                