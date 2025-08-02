"""
Example usage of Longest Increasing Subsequence (LIS) Backtracking Implementation

This script demonstrates the various LIS backtracking functions with different
examples and shows the performance differences between implementations.
"""

import time
from lis_backtracking import (
    lis_backtracking,
    lis_backtracking_with_memoization,
    lis_backtracking_all_solutions,
    lis_backtracking_count_solutions,
    lis_backtracking_optimized,
    analyze_lis_complexity,
    lis_backtracking_with_path,
    lis_backtracking_erickson_formulation,
    lis_backtracking_erickson_memoized,
    create_test_sequences
)


def demonstrate_basic_functionality():
    """Demonstrate basic LIS backtracking functionality."""
    print("=== Basic LIS Backtracking Functionality ===")
    
    # Test sequences
    test_cases = [
        ([], "Empty sequence"),
        ([1], "Single element"),
        ([1, 2, 3, 4, 5], "Strictly increasing"),
        ([5, 4, 3, 2, 1], "Strictly decreasing"),
        ([1, 3, 2, 4, 5], "Mixed sequence"),
        ([10, 22, 9, 33, 21, 50, 41, 60], "Classic example"),
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], "Complex example"),
    ]
    
    for sequence, description in test_cases:
        result = lis_backtracking(sequence)
        print(f"{description}: {sequence} -> LIS length: {result}")


def demonstrate_memoization_benefits():
    """Demonstrate the benefits of memoization."""
    print("\n=== Memoization Benefits ===")
    
    # Use a larger sequence to show performance difference
    sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 6]
    
    print(f"Testing sequence: {sequence}")
    print(f"Sequence length: {len(sequence)}")
    
    # Test basic backtracking
    start_time = time.time()
    basic_result = lis_backtracking(sequence)
    basic_time = time.time() - start_time
    
    # Test memoized version
    start_time = time.time()
    memo_result = lis_backtracking_with_memoization(sequence)
    memo_time = time.time() - start_time
    
    print(f"Basic backtracking: {basic_result} (time: {basic_time:.6f}s)")
    print(f"Memoized version: {memo_result} (time: {memo_time:.6f}s)")
    if memo_time > 0:
        print(f"Speedup: {basic_time/memo_time:.2f}x")
    else:
        print("Speedup: N/A (memoized time too small to measure)")
    print(f"Results match: {basic_result == memo_result}")


def demonstrate_all_solutions():
    """Demonstrate finding all LIS solutions."""
    print("\n=== Finding All LIS Solutions ===")
    
    test_cases = [
        ([1, 2, 3, 4, 5], "Strictly increasing"),
        ([5, 4, 3, 2, 1], "Strictly decreasing"),
        ([1, 3, 2, 4, 5], "Mixed sequence"),
    ]
    
    for sequence, description in test_cases:
        solutions = lis_backtracking_all_solutions(sequence)
        print(f"{description}: {sequence}")
        print(f"  LIS length: {len(solutions[0]) if solutions else 0}")
        print(f"  Number of solutions: {len(solutions)}")
        for i, solution in enumerate(solutions[:3]):  # Show first 3 solutions
            print(f"    Solution {i+1}: {solution}")
        if len(solutions) > 3:
            print(f"    ... and {len(solutions) - 3} more solutions")
        print()


def demonstrate_counting_solutions():
    """Demonstrate counting LIS solutions."""
    print("\n=== Counting LIS Solutions ===")
    
    test_cases = [
        ([1, 2, 3, 4, 5], "Strictly increasing"),
        ([5, 4, 3, 2, 1], "Strictly decreasing"),
        ([1, 3, 2, 4, 5], "Mixed sequence"),
        ([10, 22, 9, 33, 21, 50, 41, 60], "Classic example"),
    ]
    
    for sequence, description in test_cases:
        length, count = lis_backtracking_count_solutions(sequence)
        print(f"{description}: {sequence}")
        print(f"  LIS length: {length}")
        print(f"  Number of LIS with this length: {count}")
        print()


def demonstrate_path_finding():
    """Demonstrate finding actual LIS paths."""
    print("\n=== Finding LIS Paths ===")
    
    test_cases = [
        ([1, 2, 3, 4, 5], "Strictly increasing"),
        ([1, 3, 2, 4, 5], "Mixed sequence"),
        ([10, 22, 9, 33, 21, 50, 41, 60], "Classic example"),
    ]
    
    for sequence, description in test_cases:
        length, path = lis_backtracking_with_path(sequence)
        print(f"{description}: {sequence}")
        print(f"  LIS length: {length}")
        print(f"  One LIS path: {path}")
        
        # Verify the path is valid
        is_increasing = all(path[i] < path[i+1] for i in range(len(path)-1))
        print(f"  Path is increasing: {is_increasing}")
        print()


def demonstrate_erickson_formulation():
    """Demonstrate Erickson's formulation."""
    print("\n=== Erickson's LISbigger Formulation ===")
    
    test_cases = [
        ([1, 2, 3, 4, 5], "Strictly increasing"),
        ([10, 22, 9, 33, 21, 50, 41, 60], "Classic example"),
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], "Complex example"),
    ]
    
    for sequence, description in test_cases:
        basic_result = lis_backtracking(sequence)
        erickson_result = lis_backtracking_erickson_formulation(sequence)
        erickson_memo_result = lis_backtracking_erickson_memoized(sequence)
        
        print(f"{description}: {sequence}")
        print(f"  Basic backtracking: {basic_result}")
        print(f"  Erickson formulation: {erickson_result}")
        print(f"  Erickson memoized: {erickson_memo_result}")
        print(f"  All match: {basic_result == erickson_result == erickson_memo_result}")
        print()


def demonstrate_complexity_analysis():
    """Demonstrate complexity analysis."""
    print("\n=== Complexity Analysis ===")
    
    # Test with different sequence sizes
    test_sequences = [
        [1, 2, 3, 4, 5],  # Small
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],  # Medium
    ]
    
    for sequence in test_sequences:
        print(f"Analyzing sequence: {sequence}")
        analysis = analyze_lis_complexity(sequence)
        
        print(f"  Sequence length: {analysis['sequence_length']}")
        print(f"  Basic backtracking: {analysis['basic_backtracking']['result']} "
              f"({analysis['basic_backtracking']['time']:.6f}s)")
        print(f"  Memoized: {analysis['memoized']['result']} "
              f"({analysis['memoized']['time']:.6f}s)")
        print(f"  Optimized: {analysis['optimized']['result']} "
              f"({analysis['optimized']['time']:.6f}s)")
        print(f"  Count analysis: {analysis['count_analysis']['length']} LIS, "
              f"{analysis['count_analysis']['count']} solutions")
        print(f"  All results match: {analysis['correctness']['all_equal']}")
        print()


def demonstrate_test_sequences():
    """Demonstrate the test sequences helper function."""
    print("\n=== Test Sequences ===")
    
    sequences = create_test_sequences()
    print(f"Number of test sequences: {len(sequences)}")
    
    for i, sequence in enumerate(sequences):
        result = lis_backtracking(sequence)
        print(f"  Sequence {i+1}: {sequence} -> LIS length: {result}")


def main():
    """Main demonstration function."""
    print("Longest Increasing Subsequence (LIS) Backtracking Demonstration")
    print("=" * 60)
    
    try:
        demonstrate_basic_functionality()
        demonstrate_memoization_benefits()
        demonstrate_all_solutions()
        demonstrate_counting_solutions()
        demonstrate_path_finding()
        demonstrate_erickson_formulation()
        demonstrate_complexity_analysis()
        demonstrate_test_sequences()
        
        print("\n=== All Demonstrations Completed Successfully ===")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 