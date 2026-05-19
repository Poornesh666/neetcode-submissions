class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ("".join(char for char in s if char.isalnum())).lower()

        i = 0
        j = len(newStr) - 1

        while i < j:
            if newStr[i] != newStr[j]:
                return False

            i += 1
            j -= 1
            
        return True