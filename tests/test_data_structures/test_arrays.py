"""
Tests for Array Data Structure
"""

import pytest
from data_structures.arrays import (
    DynamicArray, two_sum, max_subarray_sum, 
    rotate_array, merge_sorted_arrays
)


class TestDynamicArray:
    """Test cases for DynamicArray implementation."""
    
    def test_initialization(self):
        """Test array initialization."""
        arr = DynamicArray()
        assert len(arr) == 0
        
        arr = DynamicArray(capacity=5)
        assert len(arr) == 0
    
    def test_append_and_access(self):
        """Test appending elements and accessing them."""
        arr = DynamicArray()
        
        # Test appending
        arr.append(1)
        arr.append(2)
        arr.append(3)
        
        assert len(arr) == 3
        assert arr[0] == 1
        assert arr[1] == 2
        assert arr[2] == 3
    
    def test_insert(self):
        """Test inserting elements at specific positions."""
        arr = DynamicArray()
        arr.append(1)
        arr.append(3)
        
        arr.insert(1, 2)
        assert arr[0] == 1
        assert arr[1] == 2
        assert arr[2] == 3
        assert len(arr) == 3
    
    def test_remove(self):
        """Test removing elements."""
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)
        
        removed = arr.remove(1)
        assert removed == 2
        assert len(arr) == 2
        assert arr[0] == 1
        assert arr[1] == 3
    
    def test_find(self):
        """Test finding elements."""
        arr = DynamicArray()
        arr.append(10)
        arr.append(20)
        arr.append(30)
        
        assert arr.find(20) == 1
        assert arr.find(40) == -1
    
    def test_resize(self):
        """Test automatic resizing."""
        arr = DynamicArray(capacity=2)
        
        # Fill beyond initial capacity
        for i in range(5):
            arr.append(i)
        
        assert len(arr) == 5
        for i in range(5):
            assert arr[i] == i


class TestArrayAlgorithms:
    """Test cases for array algorithms."""
    
    def test_two_sum(self):
        """Test two sum algorithm."""
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum(nums, target)
        assert result == [0, 1]
        
        nums = [3, 2, 4]
        target = 6
        result = two_sum(nums, target)
        assert result == [1, 2]
        
        nums = [3, 3]
        target = 6
        result = two_sum(nums, target)
        assert result == [0, 1]
    
    def test_max_subarray_sum(self):
        """Test maximum subarray sum (Kadane's algorithm)."""
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        assert max_subarray_sum(nums) == 6  # [4,-1,2,1]
        
        nums = [1]
        assert max_subarray_sum(nums) == 1
        
        nums = [5, 4, -1, 7, 8]
        assert max_subarray_sum(nums) == 23
    
    def test_rotate_array(self):
        """Test array rotation."""
        nums = [1, 2, 3, 4, 5, 6, 7]
        rotate_array(nums, 3)
        assert nums == [5, 6, 7, 1, 2, 3, 4]
        
        nums = [-1, -100, 3, 99]
        rotate_array(nums, 2)
        assert nums == [3, 99, -1, -100]
    
    def test_merge_sorted_arrays(self):
        """Test merging sorted arrays."""
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        result = merge_sorted_arrays(arr1, arr2)
        assert result == [1, 2, 3, 4, 5, 6]
        
        arr1 = [1, 2, 3]
        arr2 = []
        result = merge_sorted_arrays(arr1, arr2)
        assert result == [1, 2, 3]