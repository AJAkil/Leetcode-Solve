"""
PROBLEM: Single-Threaded CPU (LeetCode 1834 - Medium)
------------------------------------------------------
Given tasks with [enqueueTime, processingTime], CPU picks tasks by:
1. Shortest processing time first
2. If tie, smallest index first
3. CPU is idle if no tasks are available

Return order of task execution.

Example:
Input: [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]

KEY INSIGHT: Sort + Min Heap simulation.
- Sort by enqueue time to process chronologically
- Use min heap to pick task with shortest processing time
- Advance time when CPU is idle
"""

class Solution:
    """
    APPROACH: Sorting + Priority Queue Simulation
    
    INTUITION:
    - Attach original indices to tasks
    - Sort tasks by enqueue time
    - Simulate CPU: push available tasks to heap, pop shortest
    - If heap empty, jump time to next task's enqueue time
    
    TIME: O(n log n)
    SPACE: O(n)
    """
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        
        # first sort the tasks array by the enqueue time
        tasks.sort(key = lambda x: x[0])
        print(tasks)

        res, minH = [], []
        i = 0
        time = tasks[0][0] # set time to the first enqueue task

        while minH or i < len(tasks):

            # first push to the heap if we have enqueued tasks in hand
            while i < len(tasks) and tasks[i][0] <= time: # only push if time has progressed
                heapq.heappush(minH, [tasks[i][1], tasks[i][2]])
                i += 1
            #print(heapq)
            
            # then pop from the minheap/pq
            if not minH:
                time = tasks[i][0]
            else:
                passed_time, index = heapq.heappop(minH)
                res.append(index)
                time += passed_time
            
        
        return res
        