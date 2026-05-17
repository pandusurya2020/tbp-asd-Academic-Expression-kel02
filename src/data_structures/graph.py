# Graph (adjacency list terbalik: dep -> [formula yang bergantung padanya])
graph: Dict[str, List[str]] = {u: [] for u in all_nodes}

for formula, deps in self.adj.items():
    for dep in deps:
        graph[dep].append(formula)
        indegree[formula] += 1
