class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stk = [] #(idx, temp)

        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][1]:
                stk_i, stk_t = stk.pop()
                res[stk_i] = i - stk_i
            stk.append((i, t))

        return res