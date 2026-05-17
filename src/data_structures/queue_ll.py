# Graph adjacency list
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

# Hitung indegree awal
indegree = {u: 0 for u in graph}

for u in graph:
    for v in graph[u]:
        indegree[v] += 1

# Simpan hasil topological sort
result = []

# Queue (untuk algoritma Kahn)
queue = [u for u, deg in indegree.items() if deg == 0]

print("=== AWAL ===")
print("Graph      :", graph)
print("Indegree   :", indegree)
print("Queue awal :", queue)
print()

while queue:
    print("Queue sekarang :", queue)

    curr = queue.pop(0)
    print(f"Ambil node '{curr}' dari queue")

    result.append(curr)
    print("Result :", result)

    for neighbor in graph[curr]:
        print(f"\nCek tetangga '{neighbor}'")

        indegree[neighbor] -= 1
        print(
            f"Indegree '{neighbor}' dikurangi jadi",
            indegree[neighbor]
        )

        if indegree[neighbor] == 0:
            print(f"'{neighbor}' dimasukkan ke queue")
            queue.append(neighbor)

    print("\nQueue akhir loop :", queue)
    print("Indegree sekarang :", indegree)
    print("-" * 40)

print("\n=== HASIL TOPOLOGICAL SORT ===")
print(result)
