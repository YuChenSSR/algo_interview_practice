#!/usr/bin/env python3
"""
Example usage of the Algorithm Interview Practice repository.

This script demonstrates how to use the various data structures,
algorithms, and utilities provided in this repository.
"""

import sys
import os

# Add the repository root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_structures.arrays import DynamicArray, two_sum, max_subarray_sum
from data_structures.linked_lists import SinglyLinkedList, reverse_linked_list, ListNode
from algorithms.sorting import merge_sort, quick_sort, bubble_sort, SORTING_ALGORITHMS
from problems.easy import valid_parentheses, palindrome_number, best_time_to_buy_and_sell_stock
from utils.testing import compare_algorithms, generate_test_cases, print_sorting_comparison, time_execution


def demonstrate_data_structures():
    """Demonstrate basic data structure operations."""
    print("=" * 60)
    print("DATA STRUCTURES DEMONSTRATION")
    print("=" * 60)
    
    # Dynamic Array
    print("\n1. Dynamic Array:")
    arr = DynamicArray()
    for i in [10, 20, 30, 40, 50]:
        arr.append(i)
    
    print(f"Array contents: {[arr[i] for i in range(len(arr))]}")
    print(f"Length: {len(arr)}")
    arr.insert(2, 25)
    print(f"After inserting 25 at index 2: {[arr[i] for i in range(len(arr))]}")
    
    # Linked List
    print("\n2. Singly Linked List:")
    ll = SinglyLinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.append(val)
    
    print(f"Linked list: {ll.to_list()}")
    ll.insert(2, 99)
    print(f"After inserting 99 at index 2: {ll.to_list()}")


def demonstrate_algorithms():
    """Demonstrate algorithm implementations."""
    print("\n" + "=" * 60)
    print("ALGORITHMS DEMONSTRATION")
    print("=" * 60)
    
    # Array algorithms
    print("\n1. Array Algorithms:")
    
    # Two Sum
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Two Sum: nums={nums}, target={target} -> indices {result}")
    
    # Maximum Subarray
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(nums)
    print(f"Max Subarray Sum: {nums} -> {result}")
    
    # Sorting algorithms comparison
    print("\n2. Sorting Algorithms:")
    test_data = [64, 34, 25, 12, 22, 11, 90]
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort
    }
    
    results = compare_algorithms(algorithms, test_data.copy())
    for name, result in results.items():
        if result['success']:
            print(f"{name}: {result['result']} (Time: {result['time']:.6f}s)")


def demonstrate_interview_problems():
    """Demonstrate solving interview problems."""
    print("\n" + "=" * 60)
    print("INTERVIEW PROBLEMS DEMONSTRATION")
    print("=" * 60)
    
    # Valid Parentheses
    print("\n1. Valid Parentheses:")
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for case in test_cases:
        result = valid_parentheses(case)
        print(f"'{case}' -> {result}")
    
    # Palindrome Number
    print("\n2. Palindrome Number:")
    test_cases = [121, -121, 10, 0, 1221]
    for case in test_cases:
        result = palindrome_number(case)
        print(f"{case} -> {result}")
    
    # Stock Problem
    print("\n3. Best Time to Buy and Sell Stock:")
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [1, 2, 3, 4, 5]
    ]
    for case in test_cases:
        result = best_time_to_buy_and_sell_stock(case)
        print(f"{case} -> Max Profit: {result}")


def performance_comparison():
    """Compare performance of different sorting algorithms."""
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    
    # Generate test data
    import random
    small_data = [random.randint(1, 100) for _ in range(20)]
    
    print(f"\nTesting with array of size {len(small_data)}")
    print(f"Original: {small_data[:10]}..." if len(small_data) > 10 else f"Original: {small_data}")
    
    # Compare sorting algorithms
    sorting_algos = {
        'Bubble Sort': bubble_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort,
    }
    
    results = compare_algorithms(sorting_algos, small_data.copy())
    print("\nSorting Algorithm Performance:")
    for name, result in results.items():
        if result['success']:
            print(f"{name:<15}: {result['time']:.6f} seconds")
    
    print("\nComplexity Reference:")
    print_sorting_comparison()


def main():
    """Main function to run all demonstrations."""
    print("Algorithm Interview Practice - Repository Demonstration")
    print("=" * 80)
    
    try:
        demonstrate_data_structures()
        demonstrate_algorithms()
        demonstrate_interview_problems()
        performance_comparison()
        
        print("\n" + "=" * 80)
        print("DEMONSTRATION COMPLETE!")
        print("=" * 80)
        print("\nTo explore more:")
        print("1. Check out the problems/ directory for more interview questions")
        print("2. Look at data_structures/ for more implementations")
        print("3. Explore algorithms/ for additional algorithms")
        print("4. Run tests with: python -m pytest tests/")
        print("5. Create your own practice problems!")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()