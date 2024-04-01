# tests/test_main.py

import unittest
from application.main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == "__main__":
    unittest.main()