"""
PROBLEM: Asteroid Collision (LeetCode 735 - Medium)
----------------------------------------------------
Asteroids move left (<0) or right (>0) at same speed. Absolute value = size.
When they collide: smaller explodes, same size both explode.
Return final state after all collisions.

Example:
Input: [5,10,-5]
Output: [5,10] (-5 collides with 10 and explodes)

Input: [10,-10]
Output: [] (both explode)

KEY INSIGHT: Stack simulation - only right-moving can collide with left-moving.
"""

from collections import deque
class Solution:
    """
    APPROACH: Stack Simulation
    
    INTUITION:
    - Use stack to track surviving asteroids
    - Only collision: stack has positive, current is negative
    - Compare magnitudes: destroy smaller, or both if equal
    - If no collision or current survives, add to stack
    
    TIME: O(n)
    SPACE: O(n)
    """
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
        