# =============================================================================
# Modules
# =============================================================================

# Python
from io import StringIO
import sys
import unittest


# Testing
from graph import Graph

# =============================================================================
# Tests
# =============================================================================

class TestGraph(unittest.TestCase):
    def setUp(self):
        """Set up a fresh graph instance for each test."""
        self.graph = Graph()

    def test_add_vertex(self):
        """Test adding vertices to the graph."""
        self.assertTrue(self.graph.add_vertex(1))
        self.assertTrue(self.graph.add_vertex(2))
        self.assertFalse(self.graph.add_vertex(1))  # Vertex already exists
        self.assertIn(1, self.graph.adj_list)
        self.assertIn(2, self.graph.adj_list)

    def test_add_edge(self):
        """Test adding edges between vertices."""
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.assertTrue(self.graph.add_edge(1, 2))
        self.assertIn(2, self.graph.adj_list[1])
        self.assertIn(1, self.graph.adj_list[2])
        self.assertFalse(self.graph.add_edge(1, 3))  # Vertex 3 does not exist

    def test_remove_edge(self):
        """Test removing edges between vertices."""
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_edge(1, 2)
        self.assertTrue(self.graph.remove_edge(1, 2))
        self.assertNotIn(2, self.graph.adj_list[1])
        self.assertNotIn(1, self.graph.adj_list[2])
        self.assertFalse(self.graph.remove_edge(1, 3))  # Vertex 3 does not exist

    def test_remove_vertex(self):
        """Test removing a vertex and its edges."""
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_edge(1, 2)
        self.assertTrue(self.graph.remove_vertex(1))
        self.assertNotIn(1, self.graph.adj_list)
        self.assertNotIn(1, self.graph.adj_list[2])
        self.assertFalse(self.graph.remove_vertex(3))  # Vertex 3 does not exist

    def test_print_graph(self):
        """Test printing the graph."""
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_edge(1, 2)
        
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        self.graph.print_graph()
        sys.stdout = sys.__stdout__  # Reset redirect

        output = captured_output.getvalue().strip().split("\n")
        self.assertEqual(output, ['1: [2]', '2: [1]'])

if __name__ == "__main__":
    unittest.main()
