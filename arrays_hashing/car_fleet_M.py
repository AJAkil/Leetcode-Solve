from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Initialize the fleet count to 1
        count = 1

        # Create pairs of (position, speed) for each car
        pairs = [(p, s) for p, s in zip(position, speed)]

        # Sort the pairs by position in descending order
        pairs_reversed = sorted(pairs, reverse=True)
        
        # Calculate the time required for each car to reach the target
        time_list = [(target - p) / s for p, s in pairs_reversed]
        
        # Initialize pointers for the current car fleet
        j = 0
        curr = 0
        
        # Iterate through the time list to count the number of fleets
        for i in range(len(time_list)):
            # If the current car takes more time than the previous car in the fleet
            if time_list[i] > time_list[curr]:
                # Increment the fleet count
                count += 1
                # Update the current car to the new car
                curr = i

        # Return the total number of car fleets
        return count
        

        