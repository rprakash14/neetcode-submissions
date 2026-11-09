class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
    
                if abs(stack[-1]) < abs(a): # second bigger than first, so first explodes, pop stack
                    stack.pop()

                elif abs(stack[-1]) > abs(a): #first bigger than second, second should not be added to stacl
                    a = 0 

                else: # both equal to we destroy both (by pop stack and set current asteroid to 0)
                    stack.pop()
                    a = 0

            if a:
                stack.append(a)
        
        return stack 



                
