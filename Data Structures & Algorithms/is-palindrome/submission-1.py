class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i=1
        newStr=""
        for char in s:
            if char.isalnum():
                newStr += char.lower()
        
        return newStr == newStr[::-1]
                
            
