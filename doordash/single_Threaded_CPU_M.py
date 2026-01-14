class Solution:
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
        