"""
Tests for Sorting Algorithms
"""

import pytest
from algorithms.sorting import (
    bubble_sort, selection_sort, insertion_sort, merge_sort,
    quick_sort, heap_sort, counting_sort, radix_sort,
    is_sorted, generate_random_array
)


class TestSortingAlgorithms:
    """Test cases for various sorting algorithms."""
    
    # Test data
    test_cases = [
        [],  # Empty array
        [1],  # Single element
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],  # Random array
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [1, 1, 1, 1, 1],  # All equal elements
        [2, 1],  # Two elements
    ]
    
    def test_bubble_sort(self):
        """Test bubble sort implementation."""
        for test_case in self.test_cases:
            result = bubble_sort(test_case)
            assert is_sorted(result)
            assert sorted(test_case) == result
    
    def test_selection_sort(self):
        """Test selection sort implementation."""
        for test_case in self.test_cases:
            result = selection_sort(test_case)
            assert is_sorted(result)
            assert sorted(test_case) == result
    
    def test_insertion_sort(self):
        """Test insertion sort implementation."""
        for test_case in self.test_cases:
            result = insertion_sort(test_case)
            assert is_sorted(result)
            assert sorted(test_case) == result
    
    def test_merge_sort(self):
        """Test merge sort implementation."""
        for test_case in self.test_cases:
            result = merge_sort(test_case)
            assert is_sorted(result)
            assert sorted(test_case) == result
    
    def test_quick_sort(self):
        """Test quick sort implementation."""
        for test_case in self.test_cases:
            result = quick_sort(test_case)
            assert is_sorted(result)
            assert sorted(test_case) == result
    
    def test_heap_sort(self):
        """Test heap sort implementation."""
        for test_case in self.test_cases:
            result = heap_sort(test_case)
            assert is_sorted(result)
            assert sorted(test_case) == result
    
    def test_counting_sort(self):
        """Test counting sort implementation."""
        # Counting sort works best with limited range integers
        test_cases = [
            [],
            [1],
            [3, 1, 4, 1, 5, 2, 6, 5, 3],
            [0, 1, 0, 1, 0, 1],
        ]
        
        for test_case in test_cases:
            result = counting_sort(test_case)
            assert is_sorted(result)
            assert sorted(test_case) == result
    
    def test_radix_sort(self):
        """Test radix sort implementation."""
        # Radix sort works with non-negative integers
        test_cases = [
            [],
            [1],
            [170, 45, 75, 90, 2, 802, 24, 66],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
        ]
        
        for test_case in test_cases:
            result = radix_sort(test_case)
            assert is_sorted(result)
            assert sorted(test_case) == result
    
    def test_is_sorted_function(self):
        """Test the is_sorted utility function."""
        assert is_sorted([])
        assert is_sorted([1])
        assert is_sorted([1, 2, 3, 4, 5])
        assert is_sorted([1, 1, 1, 1])
        assert not is_sorted([3, 1, 2])
        assert not is_sorted([5, 4, 3, 2, 1])
    
    def test_generate_random_array(self):
        """Test random array generation."""
        arr = generate_random_array(10, 0, 100)
        assert len(arr) == 10
        assert all(0 <= x <= 100 for x in arr)
        
        arr = generate_random_array(0)
        assert len(arr) == 0
    
    def test_sorting_algorithms_with_random_data(self):
        """Test all sorting algorithms with randomly generated data."""
        algorithms = [
            bubble_sort, selection_sort, insertion_sort,
            merge_sort, quick_sort, heap_sort
        ]
        
        for _ in range(5):  # Test multiple random arrays
            test_array = generate_random_array(20, -50, 50)
            expected = sorted(test_array)
            
            for algorithm in algorithms:
                result = algorithm(test_array)
                assert result == expected, f"{algorithm.__name__} failed on {test_array}"