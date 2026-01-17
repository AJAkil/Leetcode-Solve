"""
PROBLEM: Course Schedule (LeetCode 207 - Medium)
-------------------------------------------------
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are 2 courses. To take course 1, you should have finished course 0. So it's possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are 2 courses. To take course 1, you need course 0, and to take course 0, you need 
course 1. This is a circular dependency (cycle), so it's impossible.

KEY INSIGHT: This is a CYCLE DETECTION problem in a directed graph.
- If there's a cycle, courses can't be completed (circular dependency)
- If there's no cycle, all courses can be completed
"""

class Solution:
    """
    APPROACH: DFS-based Cycle Detection with Backtracking
    
    INTUITION:
    - Build a directed graph where edge (a -> b) means "to take course a, must complete b first"
    - Use DFS to detect cycles: if we revisit a node currently in our path, there's a cycle
    - Use a visited set to track nodes in the CURRENT DFS path (not globally visited)
    - Mark processed nodes by clearing their prerequisites to avoid redundant work
    
    STEPS:
    1. Build adjacency list: prereq[course] = list of prerequisites for that course
    2. For each course, run DFS:
       a. If course is in visited set -> cycle detected (we're revisiting current path)
       b. If course has no prerequisites -> can be taken (base case)
       c. Mark course as visited (add to path)
       d. Recursively check all prerequisites
       e. If any prerequisite has cycle -> return False
       f. If all prerequisites are valid:
          - Remove from visited (backtrack - not in path anymore)
          - Clear prerequisites (optimization - mark as processed)
          - Return True
    3. If all courses can be completed without cycles -> return True
    
    TIME COMPLEXITY: O(V + E) where V = numCourses, E = prerequisites.length
    - Each course (vertex) is visited at most once due to prereq[course] = [] optimization
    - Each prerequisite edge is traversed at most once
    - Even though we loop through all courses, once a course is processed (prereq cleared),
      subsequent calls return immediately in O(1)
    
    SPACE COMPLEXITY: O(V + E)
    - Adjacency list: O(E) for storing all prerequisites
    - Visited set: O(V) in worst case (maximum depth of recursion)
    - Recursion stack: O(V) in worst case (linear chain of dependencies)
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()  # Tracks courses in CURRENT DFS path (for cycle detection)

        # Build adjacency list: prereq[course] = [list of prerequisites]
        prereq = {i: [] for i in range(numCourses)}

        for course, p in prerequisites:
            prereq[course].append(p)  # course depends on prerequisite p

        def dfs(course):
            """
            Returns True if course can be completed (no cycle in its dependency chain)
            Returns False if there's a cycle
            """
            # CYCLE DETECTION: if course is in current path, we found a cycle
            if course in visited:
                return False
            
            # BASE CASE: course has no prerequisites, can definitely be taken
            if prereq[course] == []:
                return True
            
            # Mark course as part of current DFS path
            visited.add(course)
            
            # Check all prerequisites recursively
            for pre in prereq[course]:
                if not dfs(pre):  # If any prerequisite has a cycle
                    return False
            
            # All prerequisites are valid (no cycles found)
            # BACKTRACK: remove from current path (we're done exploring this branch)
            visited.remove(course)

            # OPTIMIZATION: mark course as fully processed by clearing prerequisites
            # Future calls to this course will hit the base case immediately
            prereq[course] = []

            return True

        # Check each course - if any has a cycle, return False
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        