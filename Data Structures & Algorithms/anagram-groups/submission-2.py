class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        lst = []
        for ch in strs:
            key = ''.join(sorted(ch))

            if key not in groups:
                groups[key] = [ch]
            else:
                groups[key].append(ch)
        # for key,val in groups.items():
        #     lst.append(val)       
        # return lst      
        return list(groups.values())