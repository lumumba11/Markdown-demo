def fox_farmer_grain(start, end, items):
    """
    Iterative solution for the Fox, Farmer, and Grain problem.

    :param start: Starting location ('left' or 'right')
    :param end: Destination location ('left' or 'right')
    :param items: List of items, where 'F' is the farmer, 'G' is the grain, and 'X' is the fox
    """

    # Initialize the state of the problem
    state = {
        'left': set(items),
        'right': set()
    }

    # Define the possible moves
    moves = {
        'left_to_right': {
            'F': {'F'},
            'G': {'G'},
            'X': {'X'},
            'FG': {'F', 'G'},
            'FX': {'F', 'X'}
        },
        'right_to_left': {
            'F': {'F'},
            'G': {'G'},
            'X': {'X'},
            'FG': {'F', 'G'},
            'FX': {'F', 'X'}
        }
    }

    # Iterate until the right side has all items
    steps = 0
    while state['right'] != set(items):
        steps += 1
        print(f"Step {steps}:")
        print(f"State: {state}")

        current_location = start if steps % 2 != 0 else end
        next_location = end if steps % 2 != 0 else start

        # Move items based on the rules
        move_found = False
        for item in state[current_location].copy():
            if len(state[current_location]) == 1:
                move_type = item
            else:
                move_type = ''.join(sorted([item, 'F']))
            
            if move_type in moves[f"{current_location}_to_{next_location}"]:
                state[current_location].remove(item)
                state[next_location].add(item)
                move_found = True
                break

        # If no valid move is found, break the loop
        if not move_found:
            print("No valid move found. Terminating.")
            break

    print(f"Total steps: {steps}")

# Example usage
fox_farmer_grain('left', 'right', ['F', 'X', 'G'])
