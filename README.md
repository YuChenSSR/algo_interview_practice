# Algorithm Interview Practice

A comprehensive repository for practicing data structures and algorithms for technical interviews. This repository contains implementations of common data structures, algorithms, and interview problems to help you prepare for coding interviews.

## 📁 Repository Structure

```
algo_interview_practice/
├── data_structures/          # Core data structure implementations
│   ├── arrays/              # Array operations and problems
│   ├── linked_lists/        # Singly/doubly linked lists
│   ├── stacks/              # Stack implementations
│   ├── queues/              # Queue implementations  
│   ├── trees/               # Binary trees, BST, AVL, etc.
│   ├── graphs/              # Graph representations and traversals
│   ├── hash_tables/         # Hash table implementations
│   └── heaps/               # Min/max heaps, priority queues
├── algorithms/              # Algorithm implementations by category
│   ├── sorting/             # Sorting algorithms
│   ├── searching/           # Search algorithms
│   ├── dynamic_programming/ # DP problems and solutions
│   ├── greedy/              # Greedy algorithms
│   ├── graph_algorithms/    # Graph-specific algorithms
│   ├── string_algorithms/   # String manipulation algorithms
│   └── math/                # Mathematical algorithms
├── problems/                # Interview problems by difficulty
│   ├── easy/                # Easy level problems
│   ├── medium/              # Medium level problems
│   └── hard/                # Hard level problems
├── tests/                   # Test files for validation
├── utils/                   # Utility functions and helpers
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Basic understanding of data structures and algorithms

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YuChenSSR/algo_interview_practice.git
cd algo_interview_practice
```

2. Install dependencies (if any):
```bash
pip install -r requirements.txt  # Will be created as needed
```

### Running Tests

To run all tests:
```bash
python -m pytest tests/
```

To run specific test categories:
```bash
python -m pytest tests/test_data_structures/
python -m pytest tests/test_algorithms/
python -m pytest tests/test_problems/
```

## 📚 What's Included

### Data Structures
- **Arrays**: Dynamic arrays, operations, common patterns
- **Linked Lists**: Singly, doubly, circular linked lists
- **Stacks**: LIFO operations, applications
- **Queues**: FIFO operations, dequeue, priority queues
- **Trees**: Binary trees, BST, AVL, red-black trees
- **Graphs**: Adjacency list/matrix, directed/undirected
- **Hash Tables**: Hash functions, collision handling
- **Heaps**: Min/max heaps, heap operations

### Algorithms
- **Sorting**: Quick sort, merge sort, heap sort, etc.
- **Searching**: Binary search, linear search, variations
- **Dynamic Programming**: Classic DP problems and patterns
- **Greedy**: Greedy approach problems
- **Graph Algorithms**: DFS, BFS, shortest path, MST
- **String Algorithms**: Pattern matching, string manipulation
- **Math**: Number theory, combinatorics, probability

### Practice Problems
- **Easy**: Fundamental problems to build confidence
- **Medium**: Intermediate problems with multiple approaches
- **Hard**: Advanced problems requiring complex thinking

## 💡 How to Use This Repository

1. **Study the implementations**: Start with data structures in the `data_structures/` folder
2. **Understand algorithms**: Review algorithms in the `algorithms/` folder
3. **Practice problems**: Solve problems in the `problems/` folder by difficulty
4. **Run tests**: Validate your understanding by running the test suites
5. **Time complexity**: Each implementation includes time and space complexity analysis

## 🎯 Interview Preparation Tips

1. **Master the basics**: Ensure you understand all fundamental data structures
2. **Practice patterns**: Look for common patterns across different problems
3. **Analyze complexity**: Always consider time and space complexity
4. **Code clean**: Write readable, well-structured code
5. **Test thoroughly**: Consider edge cases and validate your solutions

## 📖 Learning Resources

- Time Complexity: Understanding Big O notation
- Space Complexity: Memory usage analysis
- Problem Patterns: Common interview question patterns
- Optimization Techniques: How to improve algorithm efficiency

## 🤝 Contributing

Feel free to contribute by:
- Adding new problems and solutions
- Improving existing implementations
- Adding test cases
- Fixing bugs or improving documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.