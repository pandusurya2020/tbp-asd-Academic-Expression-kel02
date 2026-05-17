import math
from typing import Optional, Dict, List, Tuple

class FormulaDAG:
    def __init__(self):
        self.adj: Dict[str, List[str]] = {} # formula -> [depends_on]
        self.formulas: Dict[str, str] = {} # nama -> ekspresi

    def define(self, nama: str, ekspresi: str, deps: List[str]) -> None:
        """Tambahkan formula dan dependensinya."""
        old_deps = self.adj.get(nama)
        old_expr = self.formulas.get(nama)

        self.adj[nama] = deps
        self.formulas[nama] = ekspresi

        try:
            self.topological_sort()  # akan raise jika ada siklus
        except ValueError:
            if old_deps is not None:
                self.adj[nama] = old_deps
                self.formulas[nama] = old_expr
            else:
                del self.adj[nama]
                del self.formulas[nama]
            raise

    def topological_sort(self) -> List[str]:
        all_nodes = set(self.adj.keys())
        for deps in self.adj.values():
            all_nodes.update(deps)

        indegree = {u: 0 for u in all_nodes}
        graph: Dict[str, List[str]] = {u: [] for u in all_nodes}

        for formula, deps in self.adj.items():
            for dep in deps:
                graph[dep].append(formula)
                indegree[formula] += 1

        queue = [u for u, deg in indegree.items() if deg == 0]
        result = []

        while queue:
            curr = queue.pop(0)
            result.append(curr)
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) < len(all_nodes):
            raise ValueError("Siklus ketergantungan terdeteksi")

        return result  
