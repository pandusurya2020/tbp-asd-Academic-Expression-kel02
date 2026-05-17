class Graph:

    def _init_(self):

        # adjacency list
        self.graph = {}

    # =========================
    # Tambah vertex
    # =========================
    def add_vertex(self, vertex):

        if vertex not in self.graph:
            self.graph[vertex] = []

    # =========================
    # Tambah edge/dependency
    # =========================
    def add_edge(self, source, destination):

        self.add_vertex(source)
        self.add_vertex(destination)

        self.graph[source].append(destination)

    # =========================
    # Tampilkan graph
    # =========================
    def display(self):

        print("=== FORMULA DEPENDENCY GRAPH ===")

        for vertex in self.graph:

            print(f"{vertex} -> {self.graph[vertex]}")

    # =========================
    # DFS Traversal
    # =========================
    def dfs(self, start, visited=None):

        if visited is None:
            visited = set()

        visited.add(start)

        print(start)

        for neighbor in self.graph[start]:

            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # =========================
    # BFS Traversal
    # =========================
    def bfs(self, start):

        visited = set()
        queue = []

        visited.add(start)
        queue.append(start)

        while queue:

            vertex = queue.pop(0)

            print(vertex)

            for neighbor in self.graph[vertex]:

                if neighbor not in visited:

                    visited.add(neighbor)
                    queue.append(neighbor)