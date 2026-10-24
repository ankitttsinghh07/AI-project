def hill_climbing(start, goal, graph):
    current = start

    while True:
        print("Current Node:", current)

        if current == goal:
            print("Goal Reached!")
            return

        neighbors = graph.get(current, [])

        if not neighbors:
            print("No better neighbor found. Stopping.")
            return

        next_node = max(neighbors, key=lambda x: x[1])

        if next_node[1] <= 0:
            print("No better neighbor found. Stopping.")
            return

        current = next_node[0]


graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 3)],
    'C': [('E', 8), ('F', 6)],
    'D': [('G', 4)],
    'E': [('G', 9)],
    'F': [('G', 7)],
    'G': []
}

hill_climbing('A', 'G', graph)