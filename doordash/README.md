# DoorDash Interview Patterns - Quick Reference Guide

This guide organizes DoorDash problems by pattern with short intuitions to trigger your memory.

---

## 🔥 HIGH PRIORITY PATTERNS (Based on Frequency)

### ⭐⭐⭐ CRITICAL - Multi-Source BFS on Matrix

**Why Critical**: Appears frequently (Walls and Gates, Rotting Oranges, 01 Matrix variant). Core concept for matrix problems.

### ⭐⭐⭐ CRITICAL - Tree DFS with Path Tracking

**Why Critical**: Binary Tree Max Path Sum appears very frequently. Similar pattern in many tree problems.

### ⭐⭐⭐ CRITICAL - DP with Binary Search

**Why Critical**: Max Profit Job Scheduling and variants appear repeatedly. Classic pattern.

### ⭐⭐ HIGH - Monotonic Stack

**Why Critical**: Multiple problems (132 Pattern, Asteroid Collision, Sliding Window Maximum). Versatile pattern.

---

## 📊 PATTERNS & PROBLEMS

## 1️⃣ MATRIX BFS/DFS - Graph Traversal on Grid ⭐⭐⭐

**Core Concept**: Multi-source BFS, island labeling, shortest path on matrix.

### 286. Walls and Gates (Med) - 63.6%

**Intuition**: Multi-source BFS from ALL gates simultaneously. Distance increases level by level.

- Start BFS from all gates at once (not one by one)
- Level-by-level expansion naturally gives shortest distances
- **Similar to**: 01 Matrix (find distance to nearest 0)

### 994. Rotting Oranges (Med) - 57.9% ⭐

**Intuition**: Multi-source BFS. All rotten oranges spread simultaneously. Track fresh count.

- Process all rotten at same level = 1 minute
- Decrement fresh count when orange rots
- Return -1 if fresh > 0 at end

### 827. Making A Large Island (Hard) - 56.1%

**Intuition**: Label islands with DFS, then check each 0's potential to connect islands.

- Phase 1: DFS label each island with unique ID, store area
- Phase 2: For each 0, sum unique neighbor island areas + 1
- Track maximum possible island size

**Pattern Recognition**:

- Multi-source BFS: Start from ALL sources (gates/rotten oranges) at once
- Island labeling: Use DFS to mark connected components with IDs
- **Critical for**: Any "spread from multiple sources" or "connected component" matrix problem

---

## 2️⃣ TREE DFS PATTERNS ⭐⭐⭐

**Core Concept**: Post-order DFS, path sum tracking, subtree calculations.

### 124. Binary Tree Maximum Path Sum (Hard) - 41.9% 🔥

**Intuition**: At each node, try forming path through it (left + node + right). Return only one branch to parent.

- Global max = node.val + left_max + right_max (path "turns" at node)
- Return to parent = node.val + max(left, right) (can only continue one direction)
- Use max(0, subtree) to ignore negative paths
- **VERY FREQUENTLY ASKED**

### 2049. Count Nodes With Highest Score (Med) - 52.4%

**Intuition**: DFS post-order to calculate subtree sizes. Score = product of component sizes.

- Build children adjacency list
- DFS returns subtree size
- At each node: score = left_size × right_size × (n - subtree_size)
- Track max score and count

**Pattern Recognition**:

- Path through node: calculate both subtrees, update global, return one branch
- Subtree size calculation: post-order DFS, accumulate from children

---

## 3️⃣ DYNAMIC PROGRAMMING ⭐⭐⭐

**Core Concept**: Memoized DFS with binary search optimization.

### 1235. Maximum Profit in Job Scheduling (Hard) - 54.6% 🔥

**Intuition**: Sort jobs by start time. For each job: skip it OR take it + recurse on next compatible job.

- Sort by start time (allows binary search)
- dfs(i): max profit from jobs[i:]
- Choice: max(skip job i, take job i + dfs(next_compatible))
- Binary search to find next compatible job (start >= end[i])
- **Frequently appears with variants**

### 329. Longest Increasing Path in Matrix (Hard) - 56.2%

**Intuition**: DFS with memo from each cell. Only move to strictly greater neighbors.

- No cycles (always increasing) → safe to memoize
- Try all 4 directions, take max + 1
- memo[(r,c)] = longest path starting at (r,c)

**Pattern Recognition**:

- Interval DP: Sort by time, binary search for next valid state
- Matrix DP: DFS + memo, constraint prevents cycles

---

## 4️⃣ MONOTONIC STACK ⭐⭐

**Core Concept**: Maintain stack invariant (increasing/decreasing) to efficiently track next/previous greater/smaller.

### 239. Sliding Window Maximum (Hard) - 48.3%

**Intuition**: Monotonic decreasing deque of indices. Front = max of window.

- Remove smaller elements from back (they can't be max anymore)
- Remove elements outside window from front
- Front of deque = maximum of current window
- O(n) - each element enters/exits deque once

### 456. 132 Pattern (Med) - 34.4%

**Intuition**: Scan right to left. Maintain decreasing stack. Track nums[k] as largest popped value.

- Stack holds potential nums[j] (middle, largest)
- When pushing larger, pop smaller as nums[k]
- If current < nums[k], found pattern (current is nums[i])

### 735. Asteroid Collision (Med) - 46.8%

**Intuition**: Stack simulation. Only collision: positive asteroid meets negative asteroid.

- Stack holds survivors
- Collision when: stack has positive, current is negative
- Compare magnitudes, destroy smaller (or both if equal)

**Pattern Recognition**:

- Next greater/smaller: monotonic stack with index tracking
- Sliding window max/min: monotonic deque
- Collision simulation: stack for sequential processing

---

## 5️⃣ BINARY SEARCH ⭐⭐

**Core Concept**: Search on answer space or sorted data.

### 875. Koko Eating Bananas (Med) - 49.5%

**Intuition**: Binary search on eating speed k. Check if can finish in h hours.

- Search range: [1, max(piles)]
- For each k: calculate time = sum(ceil(pile/k))
- If time ≤ h: try smaller k (search left)
- Minimize k

### 1268. Search Suggestions System (Med) - 65.1%

**Intuition**: Sort products. For each prefix, binary search for insertion point, take next 3.

- Sort lexicographically
- Binary search finds where prefix would insert
- Next 3 words (if they start with prefix) are suggestions
- **Alternative**: Trie with DFS, but sorting + binary search is simpler

**Pattern Recognition**:

- Binary search on answer: when checking feasibility is easy
- Binary search on sorted array: finding position/range efficiently

---

## 6️⃣ GREEDY / SORTING ⭐

**Core Concept**: Sort first, then make optimal local decisions.

### 56. Merge Intervals (Med) - 50.9%

**Intuition**: Sort by start time. Merge greedily if overlap.

- Sort by interval.start
- If curr.start ≤ last.end: merge (extend last.end)
- Otherwise: add as separate interval

### 826. Most Profit Assigning Work (Med) - 56.1%

**Intuition**: Sort jobs by difficulty, workers by ability. Two pointers to avoid rescanning.

- Sort both arrays
- For each worker (weak to strong): continue from previous job pointer
- Track max profit seen so far (monotonic property)
- Assign each worker their best available profit

**Pattern Recognition**:

- Interval problems: sort by start/end time
- Assignment problems: sort both arrays, use two pointers

---

## 7️⃣ HEAP / PRIORITY QUEUE ⭐

**Core Concept**: Efficiently track min/max or process in priority order.

### 1834. Single-Threaded CPU (Med) - 47.2%

**Intuition**: Sort tasks by enqueue time. Use min heap for available tasks (by processing time).

- Sort by enqueue time
- Simulate: push available tasks to heap, pop shortest
- If heap empty, jump time to next task enqueue
- Track task order by original indices

**Pattern Recognition**:

- Task scheduling: heap for priority, time simulation
- K-th element: heap maintains top k elements

---

## 8️⃣ GRAPH - TOPOLOGICAL SORT

**Core Concept**: Detect cycles, find valid ordering in DAG.

### 207. Course Schedule (Med)

**Intuition**: DFS cycle detection. If revisit node in current path → cycle.

- Build adjacency list (course → prerequisites)
- DFS with visited set for current path
- If node in visited → cycle detected
- Backtrack by removing from visited

### 210. Course Schedule II (Med)

**Intuition**: Same as Course Schedule I, but track order with post-order DFS.

- Add course to result AFTER visiting all prerequisites
- Post-order ensures prerequisites come before course
- If cycle detected → return []

**Pattern Recognition**:

- Cycle detection: DFS with visited set for current path
- Topological sort: post-order DFS adds nodes after processing dependencies

---

## 9️⃣ STRING MANIPULATION

**Core Concept**: Frequency counting, anagram checking, position tracking.

### 1790. Check if One String Swap Can Make Strings Equal (Easy) - 49.5%

**Intuition**: Count position differences. Must be exactly 2, and they swap to match.

- If frequencies differ → false (not anagrams)
- Count position diffs: must be 0 or 2
- If 2: check if swapping makes them equal
- If 0: need duplicate char to swap with itself

### 1347. Minimum Steps to Make Two Strings Anagram (Med) - 82.4%

**Intuition**: Count char frequency difference.

- For each char in t: if excess compared to s, count difference
- Sum all excesses = steps needed

### 859. Buddy Strings (Easy) - 33.9%

**Intuition**: Similar to swap problem - check frequencies and position diffs.

- Must have same frequencies
- diff == 2: can swap
- diff == 0: need duplicate char

**Pattern Recognition**:

- Anagram problems: frequency counting with Counter
- Swap problems: count position differences + frequency check

---

## 🔟 TRIE / PREFIX TREE

**Core Concept**: Hierarchical string/path storage for prefix queries.

### 1166. Design File System (Med) - 65.1% ⭐

**Intuition**: Trie where each node = directory/file. Split path by '/'.

- Each TrieNode has children dict and value
- createPath: split by '/', traverse/create nodes, check parent exists
- get: traverse path, return value or -1

**Pattern Recognition**:

- Path/directory systems: trie with '/' as separator
- Prefix search: trie traversal

---

## 🎯 FOCUS STRATEGY

Based on frequency data (last 6 months):

### 🔥 MUST MASTER (Repeatedly appears)

1. **Multi-Source BFS on Matrix** (Walls & Gates, Rotting Oranges)
   - Pattern appears in 01 Matrix and many variants

2. **Binary Tree Max Path Sum** - Explicitly mentioned as frequent
   - Master the "global max vs return to parent" pattern

3. **Job Scheduling DP** - Explicitly mentioned with variants
   - Sort + binary search + memoized DFS pattern

4. **Search Suggestions System** - Explicitly mentioned
   - Trie OR binary search approach

### ⚡ HIGH PRIORITY

5. **Sliding Window Maximum** (Monotonic deque pattern)
2. **Longest Increasing Path in Matrix** (Matrix DP with memo)
3. **Graph DFS/BFS** (Course Schedule, topological sort)

### 📝 GOOD TO KNOW

8. Stack problems (132 Pattern, Asteroid Collision)
2. Greedy (Merge Intervals, Task Assignment)
3. String manipulation (Anagram, Swap)

---

## 💡 PATTERN RECOGNITION TIPS

### When you see a matrix problem

- **Multiple sources spreading**: Multi-source BFS
- **Find connected components**: DFS with labeling
- **Shortest path**: BFS (unweighted), Dijkstra (weighted)

### When you see a tree problem

- **Path through node**: Calculate both subtrees, update global, return one
- **Subtree property**: Post-order DFS

### When you see intervals/scheduling

- **Overlapping intervals**: Sort + greedy merge
- **Non-overlapping selection**: Sort + DP with binary search

### When you see monotonic property

- **Sliding window**: Monotonic deque
- **Next greater/smaller**: Monotonic stack
- **Min/max tracking**: Heap

---

## 📚 SIMILAR LEETCODE PROBLEMS (For Extra Practice)

Based on the patterns above, these are related problems at same difficulty:

### Matrix BFS/DFS

- **542. 01 Matrix** (Nearly identical to Walls and Gates)
- **1162. As Far from Land as Possible**
- **1020. Number of Enclaves**

### Tree Path Sum

- **543. Diameter of Binary Tree**
- **687. Longest Univalue Path**

### Interval DP

- **1043. Partition Array for Maximum Sum**
- **1048. Longest String Chain**

### Monotonic Stack

- **84. Largest Rectangle in Histogram**
- **901. Online Stock Span**

---

## 🎓 FINAL TIPS

1. **Matrix BFS**: Always think "Can I start from ALL sources at once?" before doing separate BFS
2. **Tree DFS**: Distinguish "value for global answer" vs "value to return to parent"
3. **Job Scheduling**: Pattern = Sort + Binary Search + DP (appears in many forms)
4. **Monotonic Stack**: When you need "next greater/smaller", think stack
5. **Binary Search**: Not just on sorted arrays - also on "answer space" when feasible to check

Good luck with your DoorDash interviews! 🚀
