"""
Restaurant Coupons - Maximum Credits at Once

Problem: Given coupons with time intervals and credit values, find the maximum
credits that can be used simultaneously.

Example: [["10:00-11:00", "5"], ["13:00-15:00", "10"]]

Similar Problems:
- Meeting Rooms II (LeetCode 253)
- Maximum Overlapping Intervals
- Car Fleet (similar sweep line approach)
- Merge Intervals (LeetCode 56)

Approach: Sweep Line Algorithm
1. Create events for each coupon (start and end)
2. Sort events by time
3. Sweep through and track active credits
4. Return maximum seen

Time Complexity: O(n log n) - dominated by sorting
Space Complexity: O(n) - for events list
"""

def max_credits(coupons):
    """
    Find maximum credits that can be used at once.
    
    Args:
        coupons: List of [time_range, credit] e.g. [["10:00-11:00", "5"]]
    
    Returns:
        Maximum credits usable simultaneously
    """
    if not coupons:
        return 0
    
    events = []
    
    # Step 1: Parse and create events
    for time_range, credit in coupons:
        start_str, end_str = time_range.split('-')
        start_minutes = time_to_minutes(start_str)
        end_minutes = time_to_minutes(end_str)
        credit_value = int(credit)
        
        # Create START and END events
        # (time, event_type, credit)
        # event_type: 1 for START, -1 for END
        # We use 1/-1 so we can easily add/subtract from running total
        events.append((start_minutes, 1, credit_value))  # START
        events.append((end_minutes, -1, credit_value))   # END
    
    # Step 2: Sort events by time
    # Primary sort: by time (x[0])
    # Secondary sort: by -x[1] to prioritize START over END at same time
    #   - START event type = 1  → -1 = -1 (comes first)
    #   - END event type = -1   → -(-1) = +1 (comes second)
    # This handles edge-to-edge intervals: [10:00-11:00] and [11:00-12:00]
    # At 11:00, we process the new START before the old END
    events.sort(key=lambda x: (x[0], -x[1]))
    
    # Step 3: Sweep through events
    max_credit = 0
    current_credit = 0
    
    for time, event_type, credit in events:
        if event_type == 1:  # START event
            current_credit += credit
            max_credit = max(max_credit, current_credit)
        else:  # END event (event_type == -1)
            current_credit -= credit
    
    return max_credit


def max_credits_with_interval(coupons):
    """
    Find maximum credits and the time interval where it occurs.
    
    Follow-up question (1): Return the time frame.
    
    Returns:
        Tuple of (max_credits, time_interval_str)
    """
    if not coupons:
        return 0, ""
    
    events = []
    
    for time_range, credit in coupons:
        start_str, end_str = time_range.split('-')
        start_minutes = time_to_minutes(start_str)
        end_minutes = time_to_minutes(end_str)
        credit_value = int(credit)
        
        events.append((start_minutes, 1, credit_value))
        events.append((end_minutes, -1, credit_value))
    
    events.sort(key=lambda x: (x[0], -x[1]))
    
    max_credit = 0
    current_credit = 0
    interval_start = 0
    interval_end = 0
    
    # Single pass: track interval while calculating max
    for time, event_type, credit in events:
        if event_type == 1:  # START event
            current_credit += credit
            if current_credit > max_credit:
                # New max found - this is the start of max interval
                max_credit = current_credit
                interval_start = time
                interval_end = 0  # Will be updated when credit drops below max
        else:  # END event
            # If we're still at max before this END, this is where max interval ends
            if current_credit == max_credit:
                interval_end = time
            current_credit -= credit
    
    interval_str = f"{minutes_to_time(interval_start)}-{minutes_to_time(interval_end)}"
    return max_credit, interval_str


def time_to_minutes(time_str):
    """Convert 'HH:MM' to minutes from midnight."""
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes


def minutes_to_time(minutes):
    """Convert minutes from midnight to 'HH:MM'."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"


# Test cases
if __name__ == "__main__":
    print("=" * 60)
    print("Test Case 1: Non-overlapping coupons")
    print("=" * 60)
    coupons1 = [["10:00-11:00", "5"], ["13:00-15:00", "10"]]
    result1 = max_credits(coupons1)
    print(f"Input: {coupons1}")
    print(f"Output: {result1}")
    print(f"Expected: 10 (no overlap, max is the 10-credit coupon)")
    print()
    
    print("=" * 60)
    print("Test Case 2: Overlapping coupons")
    print("=" * 60)
    coupons2 = [["10:00-12:00", "5"], ["11:00-13:00", "10"]]
    result2 = max_credits(coupons2)
    print(f"Input: {coupons2}")
    print(f"Output: {result2}")
    print(f"Expected: 15 (both active during 11:00-12:00)")
    print()
    
    print("=" * 60)
    print("Test Case 3: Multiple overlaps")
    print("=" * 60)
    coupons3 = [
        ["10:00-12:00", "5"], 
        ["11:00-13:00", "10"],
        ["11:30-12:30", "7"]
    ]
    result3 = max_credits(coupons3)
    print(f"Input: {coupons3}")
    print(f"Output: {result3}")
    print(f"Expected: 22 (all three active during 11:30-12:00)")
    print()
    
    print("=" * 60)
    print("Test Case 4: Nested intervals")
    print("=" * 60)
    coupons4 = [
        ["09:00-18:00", "20"],
        ["10:00-12:00", "5"],
        ["11:00-11:30", "3"]
    ]
    result4 = max_credits(coupons4)
    print(f"Input: {coupons4}")
    print(f"Output: {result4}")
    print(f"Expected: 28 (all three active during 11:00-11:30)")
    print()
    
    print("=" * 60)
    print("Test Case 5: Single coupon")
    print("=" * 60)
    coupons5 = [["14:00-15:00", "100"]]
    result5 = max_credits(coupons5)
    print(f"Input: {coupons5}")
    print(f"Output: {result5}")
    print(f"Expected: 100")
    print()
    
    print("=" * 60)
    print("Test Case 6: Edge-to-edge (no overlap)")
    print("=" * 60)
    coupons6 = [["10:00-11:00", "5"], ["11:00-12:00", "10"]]
    result6 = max_credits(coupons6)
    print(f"Input: {coupons6}")
    print(f"Output: {result6}")
    print(f"Expected: 10 (depending on interpretation - treating end as exclusive)")
    print()
    
    print("=" * 60)
    print("Follow-up: With Time Interval")
    print("=" * 60)
    coupons7 = [["10:00-12:00", "5"], ["11:00-13:00", "10"]]
    credit, interval = max_credits_with_interval(coupons7)
    print(f"Input: {coupons7}")
    print(f"Max Credits: {credit}")
    print(f"Time Interval: {interval}")
    print()
    
    print("=" * 60)
    print("Complexity Analysis")
    print("=" * 60)
    print("Time Complexity: O(n log n)")
    print("  - Parsing: O(n)")
    print("  - Creating events: O(n)")
    print("  - Sorting events: O(n log n)")
    print("  - Sweeping: O(n)")
    print("  - Total: O(n log n)")
    print()
    print("Space Complexity: O(n)")
    print("  - Events array: O(n) - 2 events per coupon")
    print("  - Sorting space: O(log n) or O(n) depending on sort algorithm")
    print("  - Total: O(n)")


def time_to_minutes(time_str):
    hour, minute = time_str.split(':')
    hour, minute = int(hour), hour(minute)

    return hour * 60 + minute

def max_credits_w_intervals(coupons):
    events = []

    for time_range, credit in coupons:
        start_time, end_time = time_range.split('-')
        start_time = time_to_minutes(start_time)
        end_time = time_to_minutes(end_time)

        events.append(start_time, 1, credit) # start event
        events.append(end_time, -1, credit) # end time
    
    # sort by the start time first, and if start and end time match,
    # we take the start time first and then the end time
    events.sort(key=lambda x: (x[0], -x[1]))

    max_credit = 0
    res_start_time = 0
    res_end_time = 0
    current_credit = 0

    # then we sweep through the events
    for time, event_type, credit in events:
        
        if event_type == 1:
            # START event, 
            current_credit += credit

            if max_credit < current_credit:
                max_credit = current_credit
                res_start_time = time # store the current start time
                res_end_time = 0 # we set the end time to be 0, for the current max 
        elif event_type == -1:
            # END event,
            # store the end time first if the current credit is still the max
            if current_credit == credit:
                res_end_time = time 
            
            # subtract the credit from the current summation, cause we are leaving the interval
            current_credit -= credit
    
    # after this we found the results, 
    return max_credit, res_start_time, res_end_time

