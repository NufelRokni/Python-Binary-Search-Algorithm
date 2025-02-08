import unittest
from binary_search import binarySearch
import random
import time

class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        """Set up test data before each test case."""
        self.small_list = [1, 3, 5, 7, 9, 11, 13, 15]
        self.large_list = list(range(1, 10**6, 2))  # Large sorted list (odds up to 1,000,000)
        self.random_large_list = sorted(random.sample(range(1, 10**6), 10**5))  # 100,000 unique sorted numbers

    def test_element_found(self):
        """Test cases where the element is present in the list."""
        self.assertEqual(binarySearch(self.small_list, 1), 0)
        self.assertEqual(binarySearch(self.small_list, 7), 3)
        self.assertEqual(binarySearch(self.small_list, 15), 7)

    def test_element_not_found(self):
        """Test cases where the element is not in the list."""
        self.assertEqual(binarySearch(self.small_list, 2), -1)
        self.assertEqual(binarySearch(self.small_list, 8), -1)
        self.assertEqual(binarySearch(self.small_list, 16), -1)

    def test_empty_list(self):
        """Test searching in an empty list."""
        self.assertEqual(binarySearch([], 5), -1)

    def test_single_element_list(self):
        """Test lists with only one element."""
        self.assertEqual(binarySearch([5], 5), 0)
        self.assertEqual(binarySearch([5], 3), -1)

    def test_large_list(self):
        """Test binary search on a large list for performance and correctness."""
        self.assertEqual(binarySearch(self.large_list, 999999), len(self.large_list) - 1)
        self.assertEqual(binarySearch(self.large_list, 500001), 250000)
        self.assertEqual(binarySearch(self.large_list, -1), -1)  # Not in the list
        self.assertEqual(binarySearch(self.large_list, 1000000), -1)  # Even number not in odd list

    def test_random_large_list(self):
        """Test binary search on a large randomly generated sorted list."""
        target = random.choice(self.random_large_list)
        self.assertNotEqual(binarySearch(self.random_large_list, target), -1)  # Should be found
        self.assertEqual(binarySearch(self.random_large_list, 10**6 + 1), -1)  # Not in list

    def test_performance_large_list(self):
        """Measure performance on a large dataset."""
        start_time = time.time()
        binarySearch(self.large_list, 999999)  # Last element
        end_time = time.time()
        self.assertLess(end_time - start_time, 0.01)  # Should be very fast

if __name__ == '__main__':
    unittest.main()
