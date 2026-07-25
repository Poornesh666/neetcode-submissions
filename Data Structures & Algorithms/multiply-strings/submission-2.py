class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def multiply_digits(d: str, num: str) -> int:
            res = 0
            for digit in num:
                res += int(digit) * int(d)
                res *= 10

            return res//10
        
        # res = [0]*(len(num1)+len(num2))
        if len(num1) >= len(num2):
            big_num = num1 
            small_num = num2
        else:
            big_num = num2
            small_num = num1

        place = 1
        res = 0
        for d in small_num[::-1]:
            res += multiply_digits(d, big_num)*place
            place *= 10
        
        return str(res)

        

            