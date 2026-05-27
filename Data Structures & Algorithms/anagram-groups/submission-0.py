class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        tempSet = set()
        for i in range(len(strs)):
            temp = [strs[i]]
            if strs[i] not in tempSet:
                for j in range(i+1, len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]):
                        temp.append(strs[j])
                        tempSet.add(strs[j])
                res.append(temp)

        return res