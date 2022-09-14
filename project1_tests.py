import Project1 as p1
import unittest


class TestProject1(unittest.TestCase):

    def test_1(self):
        self.assertEqual(len(p1.shortestPath(p1.bfs([1, 2, 3, 4], [4, 2, 3, 2]), [
                         1, 2, 3, 4], [4, 2, 3, 2])), 3, "Should be 3")

    def test_2(self):
        self.assertEqual(len(p1.shortestPath(p1.bfs([1, 2, 3, 4], [6, 4, 3, 5]), [
                         1, 2, 3, 4], [6, 4, 3, 5])), 4, "Should be 4")

    def test_3(self):
        self.assertEqual(len(p1.shortestPath(p1.bfs([1, 2, 3, 4], [6, 6, 6, 6]), [
                         1, 2, 3, 4], [6, 6, 6, 6])), 9, "Should be 9")

    def test_4(self):
        self.assertEqual(len(p1.shortestPath(p1.bfs([6, 5, 1, 2], [1, 1, 6, 6]), [
            6, 5, 1, 2], [1, 1, 6, 6])), 6, "Should be 6")


if __name__ == "__main__":
    print("Running unit tests for Project 1 \n")
    unittest.main(verbosity=2)
    print("All tests passed")
