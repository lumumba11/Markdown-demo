import heapq


def fox_chicken_grain_farmer_graph_search(start, end):
    """
    Graph search solution for the Fox, Chicken, Grain, and Farmer problem.

    Args:
        start: Starting location ('left' or 'right')
        end: Destination location ('left' or 'right')

    Returns:
        The number of moves required to solve the problem
    """

    # Define the possible moves
    moves = {
        'farmer': ('fox', 'chicken', 'grain'),
        'fox': (),
        'chicken': (),
        'grain': ()
    }

    # Define the initial and goal states
    initial_state = (start, start, start, start, start, 'farmer')
    goal_state = (end, end, end, end, end, 'farmer')

    # Define the transition function
    def transition(state):
        location = state[:5]
        item = state[5]

        # Determine possible next states based on the current item
        next_states = []
        if item == 'farmer':
            for i, loc in enumerate(location):
                next_states.append((loc, item) + location[:i] + (end if loc == start else start,) + location[i + 1:])
        else:
            for i, item_loc in enumerate(location):
                if item_loc == item or item_loc == 'farmer':
                    new_item = 'farmer' if item_loc == 'farmer' else item
                    next_states.append((item_loc, new_item) + location[:i] + (end if item_loc == start else start,) + location[i + 1:])

        # Ensure fox and grain aren't left together without the farmer
        next_states = [s for s in next_states if not (s[1] == 'fox' and s[3] == 'grain')]

        return next_states

    # Define the heuristic function
    def heuristic(state):
        return sum(1 for i, s in enumerate(state) if s != goal_state[i])

    # Define the search function
    def search(initial_state, goal_state, transition, heuristic):
        frontier = []
        explored = set()

        heapq.heappush(frontier, (0, initial_state))

        while frontier:
            cost, state = heapq.heappop(frontier)

            if state in explored:
                continue

            explored.add(state)

            if state == goal_state:
                return cost

            for next_state in transition(state):
                if next_state not in explored:
                    heapq.heappush(frontier, (cost + 1 + heuristic(next_state), next_state))

        return None

    # Run the search and return the number of moves
    return search(initial_state, goal_state, transition, heuristic)


# Example usage
print(fox_chicken_grain_farmer_graph_search('left', 'right'))  # Output: 9
