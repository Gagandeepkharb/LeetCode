class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub: str) -> bool:
            return all(c.lower() in sub and c.upper() in sub for c in set(sub))

        n = len(s)
        longest = ""
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if is_nice(substring):
                    if len(substring) > len(longest):
                        longest = substring
        
        return longest
