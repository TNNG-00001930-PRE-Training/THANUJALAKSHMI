import unittest
import operations

class operationstest(unittest.TestCase):
    def test_concatenation(self):
        self.assertEqual(operations.concatenate("hello", "friends"), "hello friends")

    def test_slicing(self):
        self.assertEqual(operations.slice_string("hello shiv", 0, 5), "hello")

    def test_formatting(self):
        self.assertEqual(operations.format_string("Hello, {}!", "sita"), "Hello, sita!")

    def test_uppercase(self):
        self.assertEqual(operations.uppercase("welcome"), "WELCOME")

    def test_lowercase(self):
        self.assertEqual(operations.lowercase("THANUJA"), "thanuja")

    def test_strip_whitespace(self):
        self.assertEqual(operations.strip_whitespace("  hello  "), "hello")

    def test_replace_string(self):
        self.assertEqual(operations.replace_string("hello world", "world", "everyone"), "hello everyone")

if __name__== '__main__':
    unittest.main()