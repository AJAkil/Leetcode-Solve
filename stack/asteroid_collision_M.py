from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            while s and a < 0 and s[-1] > 0:
                a_mag = abs(a)

                if a_mag == s[-1]:
                    a = 0
                    s.pop()
                elif a_mag > s[-1]:
                    s.pop()
                else:
                    a = 0

            if a!=0:
                s.append(a) 
            
        return s
        