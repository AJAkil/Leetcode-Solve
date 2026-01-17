"""
PROBLEM: Maximum Profit Assignment (LeetCode 826 - Medium)
-----------------------------------------------------------
You have n jobs, where each job i is characterized by:
- difficulty[i]: the difficulty level of the job
- profit[i]: the profit you get for completing the job

You also have m workers, where each worker j has ability[j].
A worker can only complete a job if their ability is >= the job's difficulty.
Each worker can complete at most one job.

Return the maximum profit we can achieve after assigning jobs to workers.

Example:
Input: difficulty = [5,10,3,2,8], profit = [1,100,1,1,3], worker = [6,7,10]
Output: 99
Explanation: 
- Worker 6 can do jobs with difficulty [2,3,5] -> max profit is 1 (job at index 2)
- Worker 7 can do jobs with difficulty [2,3,5] -> max profit is 1
- Worker 10 can do jobs with difficulty [2,3,5,8,10] -> max profit is 100 (job at index 1)
- Total: 1 + 1 + 100 = 102 (but reassigning: 0 + 0 + 100 = 100 or optimal is 99 with different config)

Actually optimal: Worker 6->job2(profit=1), Worker 7->job2(profit=1), Worker 10->job1(profit=100) = 102
But if we can only use each job once: recalculate based on problem variant.

KEY INSIGHT: This is a TWO-POINTER problem after sorting both arrays.
- Sort jobs by difficulty and workers by ability
- For each worker, find all jobs they can do (difficulty <= ability)
- Track the maximum profit among those jobs
- Use monotonic property: if worker1 can do all jobs worker0 can do,
  then max_profit[worker1] >= max_profit[worker0]
"""

class Solution:
    """
    APPROACH: Two-Pointer with Monotonic Tracking
    
    INTUITION:
    - Sort jobs by difficulty level
    - Sort workers by ability level
    - Since both are sorted, we can use two pointers to avoid rescanning
    - As we process workers from weakest to strongest:
      * We can only do more jobs (not fewer)
      * The best profit available can only stay same or increase
      * This means we DON'T need to reset the job pointer
    - Track the maximum profit found so far as we scan through jobs
    
    ALGORITHM STEPS:
    1. Create job_indices array and sort by difficulty (preserve original profit values)
    2. Sort workers by ability
    3. Use two pointers:
       - job_i: points to current job in difficulty-sorted order
       - w: iterates through workers in ability-sorted order
    4. For each worker:
       - Continue from previous job_i (don't restart from 0)
       - Process all jobs this worker can do (difficulty <= worker[w])
       - Track the maximum profit among those jobs
       - Add this max profit to result
    5. Return total profit
    
    WHY TWO-POINTER WORKS:
    - Worker[0] (weakest) can do jobs [0..j]
    - Worker[1] (next weakest) can do jobs [0..j+1] or [0..j]
    - We never need to reconsider job 0 for worker[1]
    - The maximum profit within reachable jobs either stays same or increases
    
    EXAMPLE WALKTHROUGH:
    difficulty = [5,10,3,2,8], profit = [1,100,1,1,3], worker = [6,7,10]
    
    After sorting:
    job_indices (by difficulty): [3,2,0,4,1] -> difficulties [2,3,5,8,10]
                                              -> profits [1,1,1,3,100]
    workers sorted: [6,7,10]
    
    Process:
    - Worker 6: can do jobs with diff [2,3,5] -> profits [1,1,1] -> max_profit=1
    - Worker 7: can do jobs with diff [2,3,5] -> still max_profit=1 (no new better jobs)
    - Worker 10: can do jobs with diff [2,3,5,8,10] -> profits [1,1,1,3,100] -> max_profit=100
    - Result: 1 + 1 + 100 = 102
    
    TIME COMPLEXITY: O(n log n + m log m)
    - Sorting jobs: O(n log n)
    - Sorting workers: O(m log m)
    - Two-pointer scan: O(n + m) - each element visited at most once
    - Total: O(n log n + m log m)
    
    SPACE COMPLEXITY: O(n)
    - job_indices array: O(n)
    - Other variables: O(1)
    """
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Step 1: Create job indices and sort by difficulty
        # This preserves the mapping between difficulty and profit
        n = len(difficulty)
        res = 0
        job_indices = [i for i in range(n)]
        job_indices.sort(key=lambda job: difficulty[job])
        
        # Step 2: Sort workers by ability level
        # We process from weakest to strongest worker
        worker.sort()
        
        # Step 3: Two-pointer approach
        job_i = 0  # Points to current job in difficulty-sorted order
        prev_w_max = 0  # Max profit found for previous worker
        temp_max = 0  # Max profit for current worker
        
        for w in range(len(worker)):
            # Start with the best profit from the previous worker
            # (it's still valid since current worker is stronger)
            temp_max = prev_w_max
            
            # Continue from previous job_i (KEY optimization)
            # We don't restart from 0 because jobs we couldn't do before
            # still can't be done now if we skip them
            while job_i < n:
                # Get the difficulty of the current job
                c_w_diff = difficulty[job_indices[job_i]]
                
                # If job is too hard for this worker, stop
                # (and all following jobs are also harder, so break)
                if c_w_diff > worker[w]:
                    break
                
                # This worker can do this job - track maximum profit
                temp_max = max(temp_max, profit[job_indices[job_i]])
                job_i += 1
            
            # Add this worker's maximum profit to result
            res += temp_max
            prev_w_max = temp_max
        
        return res
        