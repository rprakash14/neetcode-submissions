class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        sort_s1 = sorted(s1)

        start = 0
        end = start + len(s1)

        while end <= len(s2):
            if sort_s1 == sorted(s2[start:end]):
                return True
            else:
                start += 1
                end +=1 
        return False
            


        