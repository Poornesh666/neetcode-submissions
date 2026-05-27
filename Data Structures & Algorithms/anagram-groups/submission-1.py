class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagramHash = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in anagramHash:
                anagramHash[key].append(s)
            else:
                anagramHash[key] = [s]

        for key,value in anagramHash.items():
            res.append(value)


        return res