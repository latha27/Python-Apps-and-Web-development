import unittest
import main


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(main.solution('A586QK', 'JJ653K'), 4)
        self.assertEqual(main.solution('23A84Q', 'K2Q25J'), 4)
        self.assertEqual(main.solution('A3A86Q', 'K2Q25J'), 6)


