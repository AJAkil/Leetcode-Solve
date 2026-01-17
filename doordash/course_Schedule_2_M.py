"""
PROBLEM: Course Schedule II (LeetCode 210 - Medium)
----------------------------------------------------
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.

Return the ordering of courses you should take to finish all courses. If there are many valid
answers, return any of them. If it's impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3] or [0,1,2,3]
Explanation: There are 4 courses. To take course 3 you need [1,2]. To take [1,2] you need course 0.
So one correct order is [0,1,2,3]. Another is [0,2,1,3].

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: []
Explanation: Circular dependency - impossible to complete.

KEY INSIGHT: This is TOPOLOGICAL SORT with cycle detection.
- Need to find a valid ordering where all prerequisites come before the course
- If there's a cycle, no valid ordering exists -> return []
"""

class Solution:
    """
    APPROACH: DFS-based Topological Sort (Postorder Traversal)
    
    INTUITION:
    - Similar to Course Schedule I, but now we need to track the ORDER
    - Use DFS postorder: add course to result AFTER visiting all its prerequisites
    - This ensures prerequisites are always added before the course that depends on them
    - The key insight: when we finish exploring a course's dependencies, we can take that course
    
    STEPS:
    1. Build adjacency list: prereq[course] = list of prerequisites
    2. Add courses with no dependencies to result first (optimization, not required)
    3. For each course, run DFS:
       a. If course in visited -> cycle detected, return False
       b. If no prerequisites -> return True (base case)
       c. Mark as visited (add to current path)
       d. Recursively visit all prerequisites
       e. If all prerequisites valid:
          - Add course to order (POSTORDER - after all dependencies)
          - Remove from visited (backtrack)
          - Clear prerequisites (mark as processed)
          - Return True
    4. If any course has cycle -> return []
    5. Otherwise return the order
    
    WHY POSTORDER WORKS:
    - Course A depends on B -> we add B to order first (during B's recursion)
    - Then we return to A and add A to order
    - Result: B appears before A in the final order ✓
    
    TIME COMPLEXITY: O(V + E) where V = numCourses, E = prerequisites.length
    - Each course (vertex) is visited at most once
    - Each prerequisite edge is traversed at most once
    - The prereq[course] = [] optimization ensures we don't revisit processed courses
    - Adding courses with no dependencies: O(V)
    
    SPACE COMPLEXITY: O(V + E)
    - Adjacency list: O(E)
    - Visited set: O(V) maximum depth
    - Order array: O(V) for the result
    - Recursion stack: O(V) in worst case
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()  # Tracks courses in CURRENT DFS path (cycle detection)
        order = []       # Stores the final course order (topological sort)
        
        # Build adjacency list
        prereq = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            prereq[course].append(pre)

        def dfs(course):
            """
            Returns True if course can be completed and adds it to order
            Returns False if there's a cycle
            """
            # CYCLE DETECTION
            if course in visited:
                return False
            
            # BASE CASE: no prerequisites, can be taken
            # Note: these are already added to order before DFS loop
            if prereq[course] == []:
                return True
            
            # Mark as part of current DFS path
            visited.add(course)

            # Recursively process all prerequisites
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            
            # POSTORDER: Add course AFTER all its prerequisites are processed
            # This ensures prerequisites appear before the course in the final order
            order.append(course)
            
            # BACKTRACK: remove from current path
            visited.remove(course)
            
            # OPTIMIZATION: mark as processed to avoid redundant work
            prereq[course] = []

            return True

        # OPTIMIZATION: Add courses with no dependencies first
        # These can be taken anytime, so add them to order upfront
        for course in prereq:
            if prereq[course] == []:
                order.append(course)
        
        # Process all courses
        for course in range(numCourses):
            if not dfs(course):
                return []  # Cycle detected - impossible to complete
        
        return order
            

        