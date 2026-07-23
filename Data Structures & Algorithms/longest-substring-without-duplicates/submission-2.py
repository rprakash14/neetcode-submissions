class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = {}
        maxLength = 0
        start = 0

        for end in range(len(s)):
            counts[s[end]] = counts.get(s[end], 0) + 1

            while counts[s[end]] > 1:
                counts[s[start]] -=1 
                start +=1
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength