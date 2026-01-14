"""
Single-Threaded CPU Task Scheduling (LeetCode 1834)

PROBLEM:
Given n tasks with enqueueTime[i] and processingTime[i], return the order (indices) in which 
tasks are executed on a single-threaded CPU. A task cannot start before its enqueue time.
When idle, the CPU picks the available task with minimum processing time.

SOLUTION STEPS:
1. Sort tasks by enqueue time (index array approach to preserve original indices)
2. Use min heap (priority queue) to track available tasks, ordered by processing time
3. Simulate CPU execution:
   - Add all tasks that have arrived (enqueueTime <= current time) to the heap
   - Pop the task with minimum processing time
   - Execute it: advance time by its processing time, record its index
   - If no tasks available, jump time to next enqueue time

INTUITION:
- Sort by enqueue time: ensures we respect "can't start before enqueue" constraint
- Min heap by processing time: greedy choice - always do shortest job available (minimizes wait)
- Simulation approach: tracks actual CPU timeline, handles gaps when no tasks are ready
- Index array: avoids modifying original task list, maintains O(1) lookups

TIME: O(n log n)  SPACE: O(n)
"""

from collections import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        
        # first sort the tasks array by the enqueue time - we need to enqueue because we can have tasks that are later enqueued but smaller processing time
        # so we need to process tasks in the order of their enqueue time
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


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        index_array = list(range(n))

        # srot the index array not the entire array
        index_array.sort(key = lambda x: (tasks[x][0], x))
        print(index_array)

        res, minH = [], []
        i = 0
        time = tasks[index_array[0]][0] # set time to the first enqueue task

        while minH or i < n:

            # first push to the heap if we have enqueued tasks in hand
            while i < n and tasks[index_array[i]][0] <= time: # only push if time has progressed
                print(index_array[i])
                heapq.heappush(minH, [tasks[index_array[i]][1], index_array[i]])
                i += 1
            #print(heapq)
            
            # then pop from the minheap/pq
            if not minH:     
                time = tasks[index_array[i]][0]
            else:
                passed_time, index = heapq.heappop(minH)
                res.append(index)
                time += passed_time
            
        
        return res
        
        