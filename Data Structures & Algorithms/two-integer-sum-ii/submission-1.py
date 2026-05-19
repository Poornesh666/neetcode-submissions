class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers) - 1

        res = [1] * 2

        while i < j:
            curr = numbers[i] + numbers[j]
            if curr == target:
                res[0] += i
                res[1] += j
                break

            if curr < target:
                i += 1

            if curr > target:
                j -= 1

        return res
            
