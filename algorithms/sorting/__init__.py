"""
Sorting Algorithms

Common sorting algorithms with different time/space complexities.
Essential for technical interviews.
"""

from typing import List
import random


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort - Simple but inefficient.
    
    Time: O(n²), Space: O(1)
    Best case: O(n) when array is already sorted
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Early termination if no swaps occurred
        if not swapped:
            break
    
    return arr


def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort - Find minimum and place at beginning.
    
    Time: O(n²), Space: O(1)
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort - Build sorted array one element at a time.
    
    Time: O(n²) average/worst, O(n) best, Space: O(1)
    Good for small arrays or nearly sorted arrays
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort - Divide and conquer approach.
    
    Time: O(n log n), Space: O(n)
    Stable sorting algorithm
    """
    if len(arr) <= 1:
        return arr.copy()
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Helper function to merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort - Efficient divide and conquer.
    
    Time: O(n log n) average, O(n²) worst, Space: O(log n)
    """
    arr = arr.copy()
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_helper(arr: List[int], low: int, high: int) -> None:
    """Helper function for quick sort."""
    if low < high:
        pivot_idx = partition(arr, low, high)
        _quick_sort_helper(arr, low, pivot_idx - 1)
        _quick_sort_helper(arr, pivot_idx + 1, high)


def partition(arr: List[int], low: int, high: int) -> int:
    """Partition function for quick sort using last element as pivot."""
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort - Uses max heap to sort.
    
    Time: O(n log n), Space: O(1)
    Not stable but in-place
    """
    arr = arr.copy()
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify(arr, i, 0)  # Call heapify on reduced heap
    
    return arr


def heapify(arr: List[int], n: int, i: int) -> None:
    """Heapify subtree rooted at index i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort - Non-comparison based sorting.
    
    Time: O(n + k), Space: O(k)
    where k is the range of input values
    Only works for integers with limited range
    """
    if not arr:
        return []
    
    min_val, max_val = min(arr), max(arr)
    range_val = max_val - min_val + 1
    
    count = [0] * range_val
    output = [0] * len(arr)
    
    # Count occurrences
    for num in arr:
        count[num - min_val] += 1
    
    # Cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output


def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort - Sort by individual digits.
    
    Time: O(d * (n + k)), Space: O(n + k)
    where d is number of digits, k is range of digits (0-9)
    """
    if not arr:
        return []
    
    max_num = max(arr)
    exp = 1
    
    arr = arr.copy()
    
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr


def counting_sort_by_digit(arr: List[int], exp: int) -> None:
    """Helper function for radix sort."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count occurrences of each digit
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    
    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy output to original array
    for i in range(n):
        arr[i] = output[i]


# Utility functions for testing and comparison
def is_sorted(arr: List[int]) -> bool:
    """Check if array is sorted."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def generate_random_array(size: int, min_val: int = 0, max_val: int = 1000) -> List[int]:
    """Generate random array for testing."""
    return [random.randint(min_val, max_val) for _ in range(size)]


# Sorting algorithm comparison
SORTING_ALGORITHMS = {
    'bubble_sort': bubble_sort,
    'selection_sort': selection_sort,
    'insertion_sort': insertion_sort,
    'merge_sort': merge_sort,
    'quick_sort': quick_sort,
    'heap_sort': heap_sort,
    'counting_sort': counting_sort,
    'radix_sort': radix_sort,
}