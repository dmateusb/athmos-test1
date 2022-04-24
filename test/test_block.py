import unittest
from models import Block

class TestBlock(unittest.TestCase):
    
    
    def test_block(self):
        list = [4, 3, 5, 6, 7, 13, 2532, 23]
        block = Block(list)
        self.assertAlmostEqual(block.max_number(), 2532)
        self.assertAlmostEqual(block.min_number(), 3)
        self.assertAlmostEqual(block.first_number(), 4)
        self.assertAlmostEqual(block.last_number(), 23)
        self.assertAlmostEqual(block.number_of_even_numbers(), 3)
        self.assertAlmostEqual(block.number_of_odd_numbers(), 5)
        self.assertAlmostEqual(block.number_of_prime_numbers(), 5)

if __name__ == '__main__':
    unittest.main()