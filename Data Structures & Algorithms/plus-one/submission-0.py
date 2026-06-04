class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tempString = ''

        for digit in digits:
            tempString += str(digit)

        newSum = int(tempString) + 1

        return list(map(int, str(newSum)))
        
        