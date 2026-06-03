class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for letter in s1:
            freq[letter] = freq.get(letter, 0) + 1

        win_size = len(s1)

        i = 0
        j = win_size

        while j <= len(s2):
            temp_str = s2[i:j]
            temp_freq = {}
            for letter in temp_str:
                temp_freq[letter] = temp_freq.get(letter, 0) + 1

            if freq == temp_freq:
                return True
                break

            i += 1
            j += 1

        return False

