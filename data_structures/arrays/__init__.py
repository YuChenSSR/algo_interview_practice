"""
Array Data Structure and Operations

Common array operations and patterns frequently asked in interviews.
"""

from typing import List, Optional, Any


class DynamicArray:
    """
    Dynamic Array implementation similar to Python's list but with explicit operations
    for interview practice.
    
    Time Complexities:
    - Access: O(1)
    - Search: O(n)
    - Insertion: O(1) amortized, O(n) worst case
    - Deletion: O(n)
    """
    
    def __init__(self, capacity: int = 10):
        """Initialize dynamic array with given capacity."""
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
    
    def __len__(self) -> int:
        """Return the size of the array."""
        return self.size
    
    def __getitem__(self, index: int) -> Any:
        """Get element at index."""
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of range")
    
    def __setitem__(self, index: int, value: Any) -> None:
        """Set element at index."""
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")
    
    def append(self, value: Any) -> None:
        """Add element to end of array. O(1) amortized."""
        if self.size >= self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1
    
    def insert(self, index: int, value: Any) -> None:
        """Insert element at specific index. O(n)."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if self.size >= self.capacity:
            self._resize()
        
        # Shift elements to right
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = value
        self.size += 1
    
    def remove(self, index: int) -> Any:
        """Remove and return element at index. O(n)."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        removed_value = self.data[index]
        
        # Shift elements to left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.size -= 1
        return removed_value
    
    def find(self, value: Any) -> int:
        """Find first occurrence of value. O(n)."""
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def _resize(self) -> None:
        """Double the array capacity."""
        old_data = self.data
        self.capacity *= 2
        self.data = [None] * self.capacity
        
        for i in range(self.size):
            self.data[i] = old_data[i]


# Common Array Problems and Solutions

def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Find two numbers that add up to target.
    
    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


def max_subarray_sum(nums: List[int]) -> int:
    """
    Find maximum sum of contiguous subarray (Kadane's Algorithm).
    
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def rotate_array(nums: List[int], k: int) -> None:
    """
    Rotate array to the right by k steps.
    
    Time: O(n), Space: O(1)
    """
    if not nums or k == 0:
        return
    
    n = len(nums)
    k = k % n
    
    # Reverse entire array
    reverse(nums, 0, n - 1)
    # Reverse first k elements
    reverse(nums, 0, k - 1)
    # Reverse remaining elements
    reverse(nums, k, n - 1)


def reverse(nums: List[int], start: int, end: int) -> None:
    """Helper function to reverse array in place."""
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Merge two sorted arrays into one sorted array.
    
    Time: O(m + n), Space: O(m + n)
    """
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result