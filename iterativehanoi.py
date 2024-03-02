def hanoi_iterative(n, source, target, auxiliary):
    """
    Iterative solution for the Tower of Hanoi problem.

    :param n: Number of disks
    :param source: Source rod
    :param target: Target rod
    :param auxiliary: Auxiliary rod
    """

    # Initialize move counter
    moves = 0

    # Initialize stacks
    source_stack = list(range(1, n + 1))
    auxiliary_stack = []
    target_stack = []

    # Main loop
    while source_stack or auxiliary_stack:
        # Move disk from source to target if possible
        if not target_stack or (source_stack and source_stack[-1] < target_stack[-1]):
            if source_stack:
                disk_to_move = source_stack.pop()
                target_stack.append(disk_to_move)
                moves += 1
                print(f"Step {moves}:")
                print(f"Source: {source_stack}")
                print(f"Auxiliary: {auxiliary_stack}")
                print(f"Target: {target_stack}\n")
        # Move disk from source to auxiliary if possible
        elif not auxiliary_stack or (source_stack and source_stack[-1] < auxiliary_stack[-1]):
            if source_stack:
                disk_to_move = source_stack.pop()
                auxiliary_stack.append(disk_to_move)
                moves += 1
                print(f"Step {moves}:")
                print(f"Source: {source_stack}")
                print(f"Auxiliary: {auxiliary_stack}")
                print(f"Target: {target_stack}\n")
        # Move disk from auxiliary to target if possible
        else:
            if auxiliary_stack:
                disk_to_move = auxiliary_stack.pop()
                target_stack.append(disk_to_move)
                moves += 1
                print(f"Step {moves}:")
                print(f"Source: {source_stack}")
                print(f"Auxiliary: {auxiliary_stack}")
                print(f"Target: {target_stack}\n")

    print(f"Total moves: {moves}")


# Example usage
hanoi_iterative(3, 'A', 'C', 'B')