import unittest
import guesser
from unittest.mock import patch


class MyTest(unittest.TestCase):
    @patch('random.randint', return_value=6)
    @patch('builtins.input', side_effect=['6'])
    def test_guesser(self, mock_input, mock_randint):
        result=guesser.guesser(2)
        self.assertEqual(result, "Correct")

if __name__=='__main__':
    unittest.main()
