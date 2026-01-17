class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # so first we sort the jobs in terms of difficulty, because we want to scan from least to
        # most difficult jobs for each worker i, upto their most difficult job that they can take at the current moment
        n = len(difficulty)
        res = 0
        job_indices = [i for i in range(n)]
        job_indices.sort(key =lambda job: difficulty[job])
        
        # then we need to sort the worker array by their ability as well, because, we want to start 
        # with the worker that has the least ability first and assign them the most profitable job they
        # can do from the available jobs upto their difficulty
        worker.sort()
        job_i = 0 # we start from 0 of the job index
        prev_w_max = 0
        temp_max = 0
        for w in range(len(worker)):
            temp_max = prev_w_max
            while job_i < n:
                # so we iterate until we are in bound for the workers ability and within the job array
                c_w_diff = difficulty[job_indices[job_i]] 

                if c_w_diff > worker[w]:
                    # if we crossed the current worker difficulty - we will start from this job_i for
                    # next worker processing
                    break
                
                temp_max = max(temp_max, profit[job_indices[job_i]])
                job_i += 1
                
            
            # after the best max profit for this worker is obtained, we can update the result
            res += temp_max
            prev_w_max = temp_max

        return res

        # [35, 47, 52, 68, 86] d
        # [17, 81, 1, 67, 3] p 
        # [10, 82, 84, 85, 92] w
        