# Queue (untuk algoritma Kahn)
queue = [u for u, deg in indegree.items() if deg == 0]

while queue:
    curr = queue.pop(0)
    result.append(curr)
    for neighbor in graph[curr]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)
