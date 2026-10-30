def minimax(depth, node, maximizing_player, values, max_depth):

    # Base condition: If leaf node is reached
    if depth == max_depth:
        return values[node]

    if maximizing_player:
        best = float('-inf')

        for i in range(2):
            val = minimax(depth + 1, node * 2 + i,
                          False, values, max_depth)
            best = max(best, val)

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = minimax(depth + 1, node * 2 + i,
                          True, values, max_depth)
            best = min(best, val)

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Maximum depth of tree
max_depth = 3

result = minimax(0, 0, True, values, max_depth)

print("The optimal value is:", result)