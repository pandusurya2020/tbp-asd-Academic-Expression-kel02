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
        
        # Deteksi siklus dengan mengecek hasil topological sort
        sorted_nodes = self.topological_sort()
        sorted_formulas = [n for n in sorted_nodes if n in self.adj]
        
        if len(sorted_formulas) < len(self.adj):
            # Jika ada siklus, kembalikan state awal
            if old_deps is not None:
                self.adj[nama] = old_deps
                self.formulas[nama] = old_expr
            else:
                del self.adj[nama]
                del self.formulas[nama]
            raise ValueError("Siklus ketergantungan terdeteksi")

    def topological_sort(self) -> List[str]:
        indegree = {u: 0 for u in self.adj}
        graph = {u: [] for u in self.adj}
        
        for formula, deps in self.adj.items():
            for dep in deps:
                if dep not in indegree:
                    indegree[dep] = 0
                if dep not in graph:
                    graph[dep] = []
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
                    
        return result
