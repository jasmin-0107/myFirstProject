import unittest
import inc_dec  # 被测试的代码

class TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 2)

    def test_increment_zero(self):
        self.assertEqual(inc_dec.increment(0), 1)

    def test_decrement_zero(self):
        self.assertEqual(inc_dec.decrement(0), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            inc_dec.increment("a")

if __name__ == "__main__":
    unittest.main()