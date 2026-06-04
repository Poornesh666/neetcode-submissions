class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tempString = ''.join(map(str, digits))

        newSum = int(tempString) + 1

        return list(map(int, str(newSum)))
        
        