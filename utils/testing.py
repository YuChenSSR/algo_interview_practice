"""
Utility functions and helpers for algorithm practice.
"""

import time
import functools
from typing import Callable, Any, List


def time_execution(func: Callable) -> Callable:
    """
    Decorator to measure function execution time.
    
    Usage:
        @time_execution
        def my_function():
            # function implementation
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper


def compare_algorithms(algorithms: dict, test_data: Any, *args, **kwargs) -> dict:
    """
    Compare multiple algorithms on the same test data.
    
    Args:
        algorithms: Dictionary of {name: function} pairs
        test_data: Input data for all algorithms
        *args, **kwargs: Additional arguments for functions
    
    Returns:
        Dictionary with timing results
    """
    results = {}
    
    for name, algorithm in algorithms.items():
        start_time = time.time()
        try:
            result = algorithm(test_data, *args, **kwargs)
            end_time = time.time()
            results[name] = {
                'time': end_time - start_time,
                'result': result,
                'success': True
            }
        except Exception as e:
            end_time = time.time()
            results[name] = {
                'time': end_time - start_time,
                'error': str(e),
                'success': False
            }
    
    return results


def generate_test_cases() -> dict:
    """
    Generate common test cases for algorithm testing.
    
    Returns:
        Dictionary containing various test case categories
    """
    return {
        'empty': [],
        'single': [1],
        'small_sorted': [1, 2, 3, 4, 5],
        'small_reverse': [5, 4, 3, 2, 1],
        'duplicates': [1, 2, 2, 3, 3, 3],
        'random_small': [3, 1, 4, 1, 5, 9, 2, 6],
        'random_medium': list(range(100, 0, -1)),
        'all_same': [5] * 10,
    }


def validate_sorted(original: List[int], sorted_array: List[int]) -> bool:
    """
    Validate that a sorted array is correct.
    
    Args:
        original: Original unsorted array
        sorted_array: Allegedly sorted array
    
    Returns:
        True if sorting is correct, False otherwise
    """
    # Check if all elements are present
    if sorted(original) != sorted_array:
        return False
    
    # Check if array is actually sorted
    for i in range(len(sorted_array) - 1):
        if sorted_array[i] > sorted_array[i + 1]:
            return False
    
    return True


def print_complexity_table():
    """Print a table of common time complexities for reference."""
    print("Common Time Complexities (Best to Worst):")
    print("-" * 50)
    print("O(1)        - Constant")
    print("O(log n)    - Logarithmic")
    print("O(n)        - Linear")
    print("O(n log n)  - Linearithmic")
    print("O(n²)       - Quadratic")
    print("O(n³)       - Cubic")
    print("O(2ⁿ)       - Exponential")
    print("O(n!)       - Factorial")
    print("-" * 50)


def print_sorting_comparison():
    """Print comparison table of sorting algorithms."""
    print("Sorting Algorithm Comparison:")
    print("-" * 80)
    print(f"{'Algorithm':<15} {'Best':<12} {'Average':<12} {'Worst':<12} {'Space':<8} {'Stable'}")
    print("-" * 80)
    
    algorithms = [
        ("Bubble Sort", "O(n)", "O(n²)", "O(n²)", "O(1)", "Yes"),
        ("Selection Sort", "O(n²)", "O(n²)", "O(n²)", "O(1)", "No"),
        ("Insertion Sort", "O(n)", "O(n²)", "O(n²)", "O(1)", "Yes"),
        ("Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(n)", "Yes"),
        ("Quick Sort", "O(n log n)", "O(n log n)", "O(n²)", "O(log n)", "No"),
        ("Heap Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(1)", "No"),
        ("Counting Sort", "O(n+k)", "O(n+k)", "O(n+k)", "O(k)", "Yes"),
        ("Radix Sort", "O(d(n+k))", "O(d(n+k))", "O(d(n+k))", "O(n+k)", "Yes"),
    ]
    
    for algo_info in algorithms:
        print(f"{algo_info[0]:<15} {algo_info[1]:<12} {algo_info[2]:<12} {algo_info[3]:<12} {algo_info[4]:<8} {algo_info[5]}")
    
    print("-" * 80)
    print("k = range of input values, d = number of digits")


class TestCase:
    """Helper class to structure test cases."""
    
    def __init__(self, input_data: Any, expected_output: Any, description: str = ""):
        self.input_data = input_data
        self.expected_output = expected_output
        self.description = description
    
    def __repr__(self):
        return f"TestCase(input={self.input_data}, expected={self.expected_output}, desc='{self.description}')"


def create_test_suite(test_cases: List[TestCase], algorithm: Callable) -> dict:
    """
    Run a test suite on an algorithm.
    
    Args:
        test_cases: List of TestCase objects
        algorithm: Function to test
    
    Returns:
        Dictionary with test results
    """
    results = {
        'passed': 0,
        'failed': 0,
        'failures': []
    }
    
    for i, test_case in enumerate(test_cases):
        try:
            if isinstance(test_case.input_data, tuple):
                result = algorithm(*test_case.input_data)
            else:
                result = algorithm(test_case.input_data)
            
            if result == test_case.expected_output:
                results['passed'] += 1
                print(f"✓ Test {i+1} passed: {test_case.description}")
            else:
                results['failed'] += 1
                failure_info = {
                    'test_case': test_case,
                    'actual_output': result,
                    'test_number': i + 1
                }
                results['failures'].append(failure_info)
                print(f"✗ Test {i+1} failed: {test_case.description}")
                print(f"  Expected: {test_case.expected_output}")
                print(f"  Got: {result}")
        
        except Exception as e:
            results['failed'] += 1
            failure_info = {
                'test_case': test_case,
                'error': str(e),
                'test_number': i + 1
            }
            results['failures'].append(failure_info)
            print(f"✗ Test {i+1} error: {test_case.description}")
            print(f"  Error: {e}")
    
    total = results['passed'] + results['failed']
    print(f"\nTest Results: {results['passed']}/{total} passed")
    
    return results