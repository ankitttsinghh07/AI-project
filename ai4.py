import heapq

def a_star(graph, heuristic, start, goal):
    # Priority queue: (f_cost, node)
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Cost from start node to current node
    g_cost = {start: 0}

    # To store the parent of each node
    parent = {start: None}

    while open_list:
        f, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g_cost[goal]

        # Explore neighbours
        for neighbour, cost in graph[current]:
            new_g_cost = g_cost[current] + cost

            if neighbour not in g_cost or new_g_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_g_cost

                # f(n) = g(n) + h(n)
                f_cost = new_g_cost + heuristic[neighbour]

                parent[neighbour] = current
                heapq.heappush(open_list, (f_cost, neighbour))

    return None, float("inf")


# Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 2)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values h(n)
heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 2,
    'F': 1,
    'G': 0
}

# Start and goal
start = 'A'
goal = 'G'

# Run A* algorithm
path, cost = a_star(graph, heuristic, start, goal)

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)