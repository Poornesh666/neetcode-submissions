class Solution:
    def reverse(self, x: int) -> int:
        str_int = str(x)

        if str_int[0] == "-":
            str_int = str_int[0] + str_int[:0:-1]
        else:
            str_int = str_int[::-1]
        
        if not (-2**31 <= int(str_int) <= 2**31 - 1): 
            return 0
        
        
        return int(str_int)
        