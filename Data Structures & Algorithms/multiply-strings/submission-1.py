class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # res = [0]*(len(num1)+len(num2))
        if len(num1) >= len(num2):
            big_num = num1 
            small_num = num2
        else:
            big_num = num2
            small_num = num1

        place = 1
        res = 0
        for num in small_num[::-1]:
            res += int(num)*int(big_num)*place
            place *= 10
        
        return str(res)
            