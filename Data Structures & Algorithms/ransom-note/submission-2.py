class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazineCounts = {}
        for char in magazine:
            if char in magazine:
                magazineCounts[char] = magazineCounts.get(char, 0) + 1
            else:
                magazineCounts[char] = 0
            
        
        for l in ransomNote:
            if l in magazineCounts and magazineCounts.get(l) > 0:
                magazineCounts[l] = magazineCounts.get(l) - 1
            else:
                return False
        return True
        

        