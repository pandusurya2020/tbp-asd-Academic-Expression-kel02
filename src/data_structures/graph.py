from typing import Dict, List

# contoh adjacency list
self_adj = {
    "F1": ["A", "B"],
    "F2": ["B"],
    "F3": ["F1"]
}

# kumpulkan semua node
all_nodes = set()

for formula, deps in self_adj.items():
    all_nodes.add(formula)

    for dep in deps:
        all_nodes.add(dep)

# graph terbalik
graph: Dict[str, List[str]] = {u: [] for u in all_nodes}

# indegree awal
indegree = {u: 0 for u in all_nodes}

# bikin reverse graph
for formula, deps in self_adj.items():

    for dep in deps:

        graph[dep].append(formula)

        indegree[formula] += 1

# debug output
print("GRAPH:")
print(graph)

print("\nINDEGREE:")
print(indegree)
