#!/usr/bin/env python3
"""
Repository Summary Script

This script provides a summary of what's available in the Algorithm Interview Practice repository.
"""

import os
import glob


def count_implementations():
    """Count various implementations in the repository."""
    counts = {
        'data_structures': 0,
        'algorithms': 0,
        'problems': 0,
        'tests': 0,
        'total_files': 0
    }
    
    # Count Python files in each category
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Data structures
    ds_files = glob.glob(os.path.join(base_path, 'data_structures', '**', '*.py'), recursive=True)
    counts['data_structures'] = len([f for f in ds_files if '__init__.py' in f])
    
    # Algorithms
    algo_files = glob.glob(os.path.join(base_path, 'algorithms', '**', '*.py'), recursive=True)
    counts['algorithms'] = len([f for f in algo_files if '__init__.py' in f])
    
    # Problems
    prob_files = glob.glob(os.path.join(base_path, 'problems', '**', '*.py'), recursive=True)
    counts['problems'] = len([f for f in prob_files if '__init__.py' in f])
    
    # Tests
    test_files = glob.glob(os.path.join(base_path, 'tests', '**', 'test_*.py'), recursive=True)
    counts['tests'] = len(test_files)
    
    # Total Python files
    all_files = glob.glob(os.path.join(base_path, '**', '*.py'), recursive=True)
    counts['total_files'] = len(all_files)
    
    return counts


def print_summary():
    """Print a comprehensive summary of the repository."""
    print("🎯 ALGORITHM INTERVIEW PRACTICE REPOSITORY")
    print("=" * 60)
    
    # File counts
    counts = count_implementations()
    
    print("\n📊 REPOSITORY STATISTICS:")
    print("-" * 30)
    print(f"📁 Total Python files: {counts['total_files']}")
    print(f"🏗️  Data structure modules: {counts['data_structures']}")
    print(f"⚙️  Algorithm modules: {counts['algorithms']}")
    print(f"❓ Problem modules: {counts['problems']}")
    print(f"✅ Test files: {counts['tests']}")
    
    print("\n🏗️  IMPLEMENTED DATA STRUCTURES:")
    print("-" * 40)
    print("✓ Dynamic Arrays (with resizing)")
    print("✓ Singly Linked Lists")
    print("✓ Doubly Linked Lists")
    print("📋 Ready for: Stacks, Queues, Trees, Graphs, Hash Tables, Heaps")
    
    print("\n⚙️  IMPLEMENTED ALGORITHMS:")
    print("-" * 30)
    print("📊 SORTING ALGORITHMS (8 implementations):")
    print("  ✓ Bubble Sort       - O(n²) time, O(1) space")
    print("  ✓ Selection Sort    - O(n²) time, O(1) space") 
    print("  ✓ Insertion Sort    - O(n²) time, O(1) space")
    print("  ✓ Merge Sort        - O(n log n) time, O(n) space")
    print("  ✓ Quick Sort        - O(n log n) avg time, O(log n) space")
    print("  ✓ Heap Sort         - O(n log n) time, O(1) space")
    print("  ✓ Counting Sort     - O(n+k) time, O(k) space")
    print("  ✓ Radix Sort        - O(d(n+k)) time, O(n+k) space")
    
    print("\n📊 ARRAY ALGORITHMS:")
    print("  ✓ Two Sum                    - O(n) time, O(n) space")
    print("  ✓ Maximum Subarray Sum       - O(n) time, O(1) space")  
    print("  ✓ Array Rotation             - O(n) time, O(1) space")
    print("  ✓ Merge Sorted Arrays        - O(m+n) time, O(m+n) space")
    
    print("\n🔗 LINKED LIST ALGORITHMS:")
    print("  ✓ Reverse Linked List        - O(n) time, O(1) space")
    print("  ✓ Find Middle Node           - O(n) time, O(1) space")
    print("  ✓ Cycle Detection            - O(n) time, O(1) space")
    print("  ✓ Merge Two Sorted Lists     - O(m+n) time, O(1) space")
    
    print("\n❓ INTERVIEW PROBLEMS (Easy Level):")
    print("-" * 40)
    print("✓ Valid Parentheses")
    print("✓ Reverse Integer")
    print("✓ Palindrome Number") 
    print("✓ Remove Duplicates from Sorted Array")
    print("✓ Merge Two Sorted Lists")
    print("✓ Maximum Depth of Binary Tree")
    print("✓ Best Time to Buy and Sell Stock")
    print("✓ Contains Duplicate")
    print("✓ Valid Anagram")
    
    print("\n🧪 TESTING & UTILITIES:")
    print("-" * 25)
    print("✓ Comprehensive pytest test suite (21 tests)")
    print("✓ Performance comparison utilities")
    print("✓ Algorithm timing decorators")
    print("✓ Test case generation")
    print("✓ Complexity reference tables")
    
    print("\n🚀 GETTING STARTED:")
    print("-" * 20)
    print("1. Run example: python example_usage.py")
    print("2. Run tests: python -m pytest tests/")
    print("3. Install deps: pip install -r requirements.txt")
    print("4. Explore: Check README.md for full guide")
    
    print("\n💡 NEXT STEPS FOR EXPANSION:")
    print("-" * 30)
    print("🔜 Medium/Hard interview problems")
    print("🔜 Binary trees and graph algorithms")
    print("🔜 Dynamic programming problems")
    print("🔜 Advanced data structures (Heaps, Tries)")
    print("🔜 String algorithms (KMP, Rabin-Karp)")
    print("🔜 Graph algorithms (Dijkstra, Floyd-Warshall)")
    
    print("\n" + "=" * 60)
    print("🎉 REPOSITORY READY FOR ALGORITHM INTERVIEW PRACTICE!")
    print("=" * 60)


if __name__ == "__main__":
    print_summary()