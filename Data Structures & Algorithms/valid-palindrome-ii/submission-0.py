class Solution:
    def validPalindrome(self, s: str) -> bool:

        delCounter = 0

        left = 0
        right = len(s) - 1
        newStr = ""
        while left < right:

            if s[left] == s[right]:
                left+=1
                right-=1
            
            elif s[left+1:right+1] == s[left+1:right+1][::-1]:
                return True

            elif s[left:right] == s[left:right][::-1]:  
                return True
            
            else:
                return False
        
        return True
        