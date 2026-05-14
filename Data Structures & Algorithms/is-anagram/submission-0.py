class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h1 = {}
        h2 = {}

        for i in s:
            h1[i] = h1.get(i, 0) + 1
            
        for i in t:
            h2[i] = h2.get(i, 0) + 1

        if h1 == h2: 
            return True
        else:
            return False
        

        