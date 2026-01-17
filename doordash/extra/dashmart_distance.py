"""
DashMart Distance Problem

Problem: City grid with DashMarts ('D'), open roads (' '), blocked roads ('X'),
and optionally customers ('C'). Find distances from given locations to nearest DashMart.

This is a variation of "Walls and Gates" (LeetCode 286) with:
- Multi-source BFS from all DashMarts
- Query specific locations
- Follow-up: Find which DashMart serves the most customers

Similar Problems:
- Walls and Gates (LeetCode 286) - EXACT SAME CONCEPT
- Rotting Oranges (LeetCode 994) - Multi-source BFS
- 01 Matrix (LeetCode 542) - Distance to nearest 0
- Shortest Distance from All Buildings (LeetCode 317)

Time Complexity: O(rows × cols) - BFS visits each cell once
Space Complexity: O(rows × cols) - for distance grid and queue
"""

from collections import deque
from typing import List, Tuple

def find_dashmart_distances(city: List[List[str]], locations: List[List[int]]) -> List[int]:
    """
    Part 1: Find distance from each location to nearest DashMart.
    
    Args:
        city: 2D grid with 'D' (DashMart), ' ' (open), 'X' (blocked)
        locations: List of [row, col] coordinates to query
    
    Returns:
        List of distances (-1 if unreachable or out of bounds)
    
    Example:
        city = [['D', ' ', 'X'],
                [' ', ' ', ' '],
                ['X', ' ', 'D']]
        locations = [[1, 1], [0, 2], [5, 5]]
        Output: [1, -1, -1]  (distance 1, blocked, out of bounds)
    """
    if not city or not city[0]:
        return [-1] * len(locations)
    
    rows, cols = len(city), len(city[0])
    
    # Distance grid: -1 = unvisited/blocked, 0 = DashMart, n = distance
    distance = [[-1] * cols for _ in range(rows)]
    queue = deque()
    
    # Step 1: Initialize - find all DashMarts and add to queue
    for r in range(rows):
        for c in range(cols):
            if city[r][c] == 'D':
                distance[r][c] = 0
                queue.append((r, c, 0))  # (row, col, dist)
            elif city[r][c] == 'X':
                distance[r][c] = -1  # Mark blocked as -1
    
    # Step 2: Multi-source BFS from all DashMarts
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check bounds and if cell is unvisited (distance == -1 but not blocked)
            if 0 <= nr < rows and 0 <= nc < cols:
                # Only visit if it's open road and not yet visited
                if city[nr][nc] != 'X' and distance[nr][nc] == -1:
                    distance[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))
    
    # Step 3: Query the given locations
    result = []
    for row, col in locations:
        # Check if location is out of bounds
        if 0 <= row < rows and 0 <= col < cols:
            result.append(distance[row][col])
        else:
            result.append(-1)  # Out of bounds
    
    return result


def find_dashmart_with_most_customers(city: List[List[str]]) -> Tuple[int, List[int]]:
    """
    Part 2 (Follow-up): Find which DashMart serves the most customers.
    
    Each customer ('C') is served by their nearest DashMart.
    Returns the count and coordinates of the DashMart serving most customers.
    
    Args:
        city: 2D grid with 'D' (DashMart), ' ' (open), 'X' (blocked), 'C' (customer)
    
    Returns:
        Tuple of (max_customers, [row, col] of best DashMart)
    
    Approach:
        - During BFS, track which DashMart each cell comes from
        - For each customer, increment count for their nearest DashMart
        - Return DashMart with highest count
    
    How Source Propagation Works:
        DashMart D at (0,0) → expands to neighbors
        
        Step 1: source_dashmart[0][0] = (0,0)  [D points to itself]
        Step 2: Visit (0,1) from (0,0)
                current_source = source_dashmart[0][0] = (0,0)  ← Original D!
                source_dashmart[0][1] = (0,0)  ← Inherit the original
        Step 3: Visit (0,2) from (0,1)
                current_source = source_dashmart[0][1] = (0,0)  ← STILL original!
                source_dashmart[0][2] = (0,0)  ← All cells trace back to (0,0)
        
        The source VALUE propagates, not the current coordinate!
    """
    if not city or not city[0]:
        return 0, [-1, -1]
    
    rows, cols = len(city), len(city[0])
    
    # Track: distance and source DashMart for each cell
    distance = [[-1] * cols for _ in range(rows)]
    source_dashmart = [[None] * cols for _ in range(rows)]  # Stores (r, c) of DashMart
    
    queue = deque()
    dashmart_locations = []  # Track all DashMart locations
    
    # Step 1: Find all DashMarts
    for r in range(rows):
        for c in range(cols):
            if city[r][c] == 'D':
                distance[r][c] = 0
                source_dashmart[r][c] = (r, c)  # Source is itself
                queue.append((r, c, 0))
                dashmart_locations.append((r, c))
            elif city[r][c] == 'X':
                distance[r][c] = -1
    
    # Step 2: Multi-source BFS - track which DashMart each cell comes from
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c, dist = queue.popleft()
        current_source = source_dashmart[r][c]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if city[nr][nc] != 'X' and distance[nr][nc] == -1:
                    distance[nr][nc] = dist + 1
                    source_dashmart[nr][nc] = current_source  # Inherit source
                    queue.append((nr, nc, dist + 1))
    
    # Step 3: Count customers per DashMart
    customer_count = {}  # {(dash_r, dash_c): count}
    
    for r in range(rows):
        for c in range(cols):
            if city[r][c] == 'C':
                # Find which DashMart serves this customer
                dash = source_dashmart[r][c]
                if dash:  # If reachable
                    customer_count[dash] = customer_count.get(dash, 0) + 1
    
    # Step 4: Find DashMart with most customers
    if not customer_count:
        return 0, [-1, -1]
    
    max_dash = max(customer_count.items(), key=lambda x: x[1])
    max_location, max_count = max_dash
    
    return max_count, list(max_location)


def visualize_distances(city: List[List[str]], distance: List[List[int]]):
    """
    Helper to visualize the distance grid.
    """
    rows, cols = len(city), len(city[0])
    
    print("\nCity Grid:")
    for row in city:
        print(' '.join(row))
    
    print("\nDistance Grid:")
    for r in range(rows):
        row_str = []
        for c in range(cols):
            if city[r][c] == 'X':
                row_str.append(' X')
            elif city[r][c] == 'D':
                row_str.append(' D')
            else:
                row_str.append(f'{distance[r][c]:2}' if distance[r][c] != -1 else ' -')
        print(' '.join(row_str))
    print()


def visualize_source_propagation(city: List[List[str]]):
    """
    DEBUGGING HELPER: Visualize how source DashMart propagates through BFS.
    Shows that each cell correctly tracks its source DashMart.
    """
    if not city or not city[0]:
        return
    
    rows, cols = len(city), len(city[0])
    
    distance = [[-1] * cols for _ in range(rows)]
    source_dashmart = [[None] * cols for _ in range(rows)]
    
    queue = deque()
    
    # Find all DashMarts
    for r in range(rows):
        for c in range(cols):
            if city[r][c] == 'D':
                distance[r][c] = 0
                source_dashmart[r][c] = (r, c)  # DashMart points to itself
                queue.append((r, c, 0))
            elif city[r][c] == 'X':
                distance[r][c] = -1
    
    # Multi-source BFS with tracking
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    print("\n=== SOURCE PROPAGATION TRACE ===\n")
    step = 0
    
    while queue:
        r, c, dist = queue.popleft()
        current_source = source_dashmart[r][c]
        
        print(f"Step {step}: Processing ({r},{c})")
        print(f"  current_source = source_dashmart[{r}][{c}] = {current_source}")
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if city[nr][nc] != 'X' and distance[nr][nc] == -1:
                    distance[nr][nc] = dist + 1
                    source_dashmart[nr][nc] = current_source  # Inherit!
                    queue.append((nr, nc, dist + 1))
                    print(f"  → Visiting neighbor ({nr},{nc})")
                    print(f"     source_dashmart[{nr}][{nc}] = {current_source} (inherited!)")
        
        step += 1
        if step > 15:  # Limit output for large grids
            print("  ... (truncated for brevity)")
            break
    
    # Show final source grid
    print("\n=== FINAL SOURCE GRID ===")
    print("Each cell shows which DashMart (row,col) it belongs to:\n")
    for r in range(rows):
        row_str = []
        for c in range(cols):
            if city[r][c] == 'X':
                row_str.append("   X  ")
            elif source_dashmart[r][c]:
                src = source_dashmart[r][c]
                row_str.append(f"({src[0]},{src[1]})")
            else:
                row_str.append("  -  ")
        print('  '.join(row_str))
    print()


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Test Case 1: Example from problem")
    print("=" * 80)
    
    city1 = [
        ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'],
        ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
        [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
        [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
    ]
    
    locations1 = [[200, 200], [1, 4], [0, 3], [5, 8], [1, 8], [5, 5]]
    result1 = find_dashmart_distances(city1, locations1)
    
    print(f"Locations: {locations1}")
    print(f"Distances: {result1}")
    print(f"Expected:  [-1, 2, 0, -1, 6, 9]")
    print()
    
    print("=" * 80)
    print("Test Case 2: Simple grid")
    print("=" * 80)
    
    city2 = [
        ['D', ' ', 'X'],
        [' ', ' ', ' '],
        ['X', ' ', 'D']
    ]
    
    locations2 = [[0, 0], [1, 1], [0, 2], [5, 5], [2, 1]]
    result2 = find_dashmart_distances(city2, locations2)
    
    visualize_distances(city2, [[-1]*3 for _ in range(3)])  # Just for display
    
    print(f"Locations: {locations2}")
    print(f"Distances: {result2}")
    print(f"Expected:  [0, 1, -1 (blocked), -1 (out of bounds), 1]")
    print()
    
    print("=" * 80)
    print("DEBUGGING: Source Propagation Visualization")
    print("=" * 80)
    print("This shows how the source DashMart coordinates propagate correctly!")
    
    city_debug = [
        ['D', ' ', ' ', ' '],
        [' ', ' ', 'X', ' '],
        [' ', ' ', ' ', 'D']
    ]
    
    visualize_source_propagation(city_debug)
    print("Notice: All reachable cells from (0,0) show (0,0)")
    print("        All reachable cells from (2,3) show (2,3)")
    print()
    
    print("=" * 80)
    print("Test Case 3: Follow-up - DashMart with most customers")
    print("=" * 80)
    
    city3 = [
        ['D', ' ', 'C', ' ', 'C'],
        [' ', ' ', 'X', ' ', ' '],
        ['C', ' ', 'X', ' ', 'C'],
        [' ', ' ', ' ', ' ', ' '],
        ['C', ' ', 'C', ' ', 'D']
    ]
    
    max_count, best_dashmart = find_dashmart_with_most_customers(city3)
    
    print("City with customers:")
    for row in city3:
        print(' '.join(row))
    print()
    print(f"DashMart serving most customers: {best_dashmart}")
    print(f"Number of customers served: {max_count}")
    print()
    
    print("=" * 80)
    print("Test Case 4: Follow-up - Multiple DashMarts")
    print("=" * 80)
    
    city4 = [
        ['D', ' ', 'C', 'X', 'D', ' ', 'C'],
        [' ', 'C', ' ', 'X', ' ', 'C', ' '],
        ['C', ' ', 'C', 'X', 'C', ' ', 'C']
    ]
    
    max_count4, best_dashmart4 = find_dashmart_with_most_customers(city4)
    
    print("City:")
    for row in city4:
        print(' '.join(row))
    print()
    print(f"Best DashMart location: {best_dashmart4}")
    print(f"Customers served: {max_count4}")
    print()
    
    print("=" * 80)
    print("Complexity Analysis")
    print("=" * 80)
    print()
    print("Part 1: Find distances to nearest DashMart")
    print("  Time:  O(R × C) - BFS visits each cell once")
    print("  Space: O(R × C) - distance grid + queue")
    print()
    print("Part 2: Find DashMart with most customers")
    print("  Time:  O(R × C) - same BFS + count customers")
    print("  Space: O(R × C) - distance + source grids")
    print()
    print("Why Multi-source BFS?")
    print("  - Start from ALL DashMarts simultaneously")
    print("  - Guarantees shortest path to nearest DashMart")
    print("  - Each cell visited exactly once")
    print("  - Better than running single-source BFS from each location")
    print()
    
    print("=" * 80)
    print("Similar Problems to Practice")
    print("=" * 80)
    print("1. Walls and Gates (LC 286) - EXACT same concept")
    print("2. Rotting Oranges (LC 994) - Multi-source BFS")
    print("3. 01 Matrix (LC 542) - Distance to nearest 0")
    print("4. Shortest Distance from All Buildings (LC 317)")
    print("5. As Far from Land as Possible (LC 1162)")


def dashmar(locations, city):
    ROWS = len(city)
    COLS = len(city[0])
    Q = deque()
    visited = set()

    dirs = [
        (-1, 0),
    (0, -1),    (0,1),
        (1,0)
    ]

    res = []
    nearest_dashmart = [[None]*COLS for _ in range(ROWS)] # stores the. (r,c) for the nearest dashmarts

    # first fill the Q with the dashmart coords
    for i in range(ROWS):
        for j in range(COLS):
            if city[i][j] == 'D':
                Q.append((i,j))
                city[i][j] = 0
                visited.add((i,j))
                nearest_dashmart[i][j] = (i,j)
    

    dist = 0
    while Q:
        n = len(Q)

        for _ in range(n):
            r,c = Q.popleft()
            current_nearest_dashmart = nearest_dashmart[r][c]
            city[r][c] = dist # for dashmarts, it will be 0

            for dir_r, dir_c in dirs:
                n_r = r + dir_r 
                n_c = c + dir_c 

                if 0 <= n_r < ROWS and 0 <= n_c < COLS and city[n_r][n_c]!='X' and (n_r, n_c) not in visited:
                    visited.add((n_r,n_c))
                    Q.append((n_r,n_c))
                    nearest_dashmart[n_r][n_c] = current_nearest_dashmart
                
        dist += 1
    

    # after we fill in the distances from the dashmarts, we fill the res
    for i,j in locations:
        if 0 <= i < ROWS and 0 <= j < COLS:
            res.append(city[i][j])
        else:
            res.append(-1)
    
    dashmart_to_customer_counts = {}

    for i in range(ROWS):
        for j in range(COLS):
            if city[i][j] == 'C':
                nearest_dashmart_coords = nearest_dashmart[i][j]
                if nearest_dashmart_coords:
                    dashmart_to_customer_counts[nearest_dashmart_coords] = dashmart_to_customer_counts.get(nearest_dashmart_coords, 0) + 1
    
    # get the coordiante of the dash with max customer counts
    dash_w_max_c = max(dashmart_to_customer_counts.items(), key=lambda x: x[1])
    
    return res, dash_w_max_c

