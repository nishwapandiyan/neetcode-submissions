from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_ct = Counter(words[0])

        for word in words[1:]:
            common_ct &= Counter(word)
        res = list(common_ct.elements())
        return res    