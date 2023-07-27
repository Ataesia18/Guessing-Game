import unittest
from guessing_game import generate_secret_number


class TestGenerateSecretNumber(unittest.TestCase):
    def test_generate_secret_number(self):
        for _ in range(1000):
            secret_number = generate_secret_number()
            self.assertTrue(1 <= secret_number <= 3)


if __name__ == "__main__":
    unittest.main()
