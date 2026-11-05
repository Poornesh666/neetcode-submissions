class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        if s == t:
            return s

        t_count = Counter(t)
        required = len(t_count)
        formed = 0
        window_counts = defaultdict(int)

        # length, left, right
        ans = float("inf"), None, None

        l, r = 0, 0

        while r < len(s):
            char = s[r]
            window_counts[char] += 1
            
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]

                if (r-l+1) < ans[0]:
                    ans = r-l+1, l, r

                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                
                l += 1
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
