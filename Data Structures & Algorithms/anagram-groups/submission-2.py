class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagramHash = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            anagramHash[key].append(s)
        
        for key,values in anagramHash.items():
            res.append(values)

        return res