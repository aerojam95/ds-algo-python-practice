# =============================================================================
# Classes
# =============================================================================

class Graph:
    """Graph implementation with basic operations."""

    def __init__(self) -> None:
        """Initialize an empty graph."""
        self.adj_list: dict[int, list[int]] = {}
        
    def print_graph(self):
        """Print the adjacency list of the graph.
        """
        for vertex, edges in self.adj_list.items():
            print(f"{vertex}: {edges}")

    def add_vertex(self, vertex: int) -> bool:
        """
        Add a new vertex to the graph.

        Args:
            vertex (int): The value of the new vertex.

        Returns:
            bool: True if the operation was successful.
        """
        if vertex in self.adj_list:
            return False
        self.adj_list[vertex] = []
        return True

    def add_edge(self, vertex1: int, vertex2: int) -> bool:
        """
        Add a new edge between two vertices in the graph.

        Args:
            vertex1 (int): The value of the first vertex.
            vertex2 (int): The value of the second vertex.

        Returns:
            bool: True if the operation was successful.
        """
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            return False
        if vertex2 not in self.adj_list[vertex1]:
            self.adj_list[vertex1].append(vertex2)
        if vertex1 not in self.adj_list[vertex2]:
            self.adj_list[vertex2].append(vertex1)
        return True

    def remove_edge(self, vertex1: int, vertex2: int) -> bool:
        """
        Remove an edge between two vertices in the graph.

        Args:
            vertex1 (int): The value of the first vertex.
            vertex2 (int): The value of the second vertex.

        Returns:
            bool: True if the operation was successful.
        """
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            return False
        self.adj_list[vertex1] = [
            vertex for vertex in self.adj_list[vertex1] if vertex != vertex2
        ]
        self.adj_list[vertex2] = [
            vertex for vertex in self.adj_list[vertex2] if vertex != vertex1
        ]
        return True

    def remove_vertex(self, vertex: int) -> bool:
        """
        Remove a vertex and all its edges from the graph.

        Args:
            vertex (int): The value of the vertex to remove.

        Returns:
            bool: True if the operation was successful.
        """
        if vertex not in self.adj_list:
            return False
        self.adj_list.pop(vertex)
        for adjacent_vertex in self.adj_list:
            self.adj_list[adjacent_vertex] = [
                v for v in self.adj_list[adjacent_vertex] if v != vertex
            ]
        return True