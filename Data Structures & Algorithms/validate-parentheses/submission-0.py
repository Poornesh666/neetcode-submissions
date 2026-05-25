class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []

        for char in s:
            if char in closeToOpen:
                if len(stack) == 0: 
                    return False
                
                if stack.pop() != closeToOpen[char]:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0