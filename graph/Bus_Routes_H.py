class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        '''
        Resource: https://www.youtube.com/watch?v=-e_PJ-G-tyU&t=1273s
        '''
        # form the dictionary first
        stop_to_routes = {}
        for route_idx in range(len(routes)):
            for stop in routes[route_idx]:
                if stop not in stop_to_routes:
                    stop_to_routes[stop] = set()

                stop_to_routes[stop].add(route_idx)
        
        # if source == target then we dont switch buses and the stops can be outside the routes
        if source == target:
            return 0

        # edge case here
        if source not in stop_to_routes or target not in stop_to_routes:
            return -1
        
        # bfs
        visited_stops, visited_routes = set(), set()
        Q = [(source, 0)] # (stop, buses taken so far)

        while len(Q) > 0:
            curr_stop, buses_taken = Q.pop(0)

            if curr_stop not in visited_stops:
                # first check if we reached the target
                print(curr_stop, buses_taken)
                if curr_stop == target:
                    #print(buses_taken)
                    return buses_taken
                
                # add to the visited stop
                visited_stops.add(curr_stop)
            
                # The main tricky part - add all the possible unvisited stops on the route of the curr_stop         
                # if the route is unvisited so far
                #print(stop_to_routes)
                for curr_route in stop_to_routes[curr_stop]:
                    if curr_route not in visited_routes:
                        # get all the stops of the current route and add it to the Q
                        for stop in routes[curr_route]:
                            if stop not in visited_stops:
                                Q.append((stop, buses_taken + 1))
                
                        # After the loop, we can consider the entire bus route has been visited
                        visited_routes.add(curr_route)

        return -1


        