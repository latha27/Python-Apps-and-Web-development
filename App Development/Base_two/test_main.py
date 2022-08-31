import unittest
import main as df


class TestBaseToBase(unittest.TestCase):

    def test_int_to_base_generator(self):
        self.assertEqual(df.int_to_base_generator([1, 0, 0, 1, 1, 1]), [1, 0, 1, 0, 1, 1])
        self.assertEqual(df.int_to_base_generator([1, 0, 0, 1, 1]), [1, 0, 1])




