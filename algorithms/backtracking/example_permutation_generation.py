"""
Example script demonstrating permutation generation algorithms.

This script shows various approaches to generating permutations using backtracking,
including performance comparisons and practical applications.
"""

import time
from permutation_generation import (
    permutation_generation_backtracking,
    permutation_generation_inplace_swap,
    permutation_generation_with_duplicates,
    permutation_generation_lexicographic,
    permutation_generation_count_only,
    permutation_generation_with_constraints,
    permutation_generation_optimized,
    permutation_generation_with_memoization,
    analyze_permutation_complexity,
    create_test_permutations
)


def demonstrate_basic_functionality():
    """Demonstrate basic permutation generation functionality."""
    print("=== Basic Permutation Generation ===\n")
    
    test_cases = [
        ([1, 2, 3], "Three elements"),
        ([1, 2], "Two elements"),
        ([1], "Single element"),
        ([], "Empty list"),
    ]
    
    for elements, description in test_cases:
        print(f"\n{description}: {elements}")
        
        # Test different approaches
        backtrack_result = permutation_generation_backtracking(elements)
        swap_result = permutation_generation_inplace_swap(elements)
        optimized_result = permutation_generation_optimized(elements)
        
        print(f"Backtracking: {len(backtrack_result)} permutations")
        print(f"In-place swap: {len(swap_result)} permutations")
        print(f"Optimized: {len(optimized_result)} permutations")
        
        # Verify all approaches give same result
        all_same = (len(backtrack_result) == len(swap_result) == len(optimized_result))
        print(f"All approaches consistent: {all_same}")
        
        if elements:
            print(f"Sample permutation: {backtrack_result[0] if backtrack_result else 'N/A'}")


def demonstrate_duplicate_handling():
    """Demonstrate handling of duplicate elements."""
    print("\n=== Duplicate Handling ===\n")
    
    test_cases = [
        ([1, 1, 2], "Two duplicates"),
        ([1, 1, 1], "All duplicates"),
        ([1, 2, 2], "One duplicate"),
    ]
    
    for elements, description in test_cases:
        print(f"\n{description}: {elements}")
        
        # Regular approach (may have duplicates)
        regular_result = permutation_generation_backtracking(elements)
        
        # Duplicate-aware approach
        unique_result = permutation_generation_with_duplicates(elements)
        
        print(f"Regular approach: {len(regular_result)} permutations")
        print(f"Unique approach: {len(unique_result)} permutations")
        print(f"Duplicates removed: {len(regular_result) - len(unique_result)}")
        
        if unique_result:
            print(f"Sample unique permutation: {unique_result[0]}")


def demonstrate_lexicographic_generation():
    """Demonstrate lexicographic permutation generation."""
    print("\n=== Lexicographic Generation ===\n")
    
    elements = [1, 2, 3]
    print(f"Elements: {elements}")
    
    result = permutation_generation_lexicographic(elements)
    print(f"Generated {len(result)} permutations in lexicographic order:")
    
    for i, perm in enumerate(result):
        print(f"  {i+1}. {perm}")


def demonstrate_constraint_handling():
    """Demonstrate constraint-based permutation generation."""
    print("\n=== Constraint Handling ===\n")
    
    # Example: Generate permutations where first element is less than last element
    elements = [1, 2, 3, 4]
    
    def constraint_func(partial):
        if len(partial) >= 2:
            return partial[0] < partial[-1]
        return True
    
    result = permutation_generation_with_constraints(elements, constraint_func)
    
    print(f"Original elements: {elements}")
    print(f"Total permutations: {permutation_generation_count_only(len(elements))}")
    print(f"Valid permutations: {len(result)}")
    print(f"Sample valid permutations:")
    for i, perm in enumerate(result[:5]):
        print(f"  {i+1}. {perm}")


def demonstrate_performance_comparison():
    """Demonstrate performance comparison between different approaches."""
    print("\n=== Performance Comparison ===\n")
    
    test_cases = [
        ([1, 2, 3], "Small (3 elements)"),
        ([1, 2, 3, 4], "Medium (4 elements)"),
    ]
    
    for elements, description in test_cases:
        print(f"\n{description}: {elements}")
        
        analysis = analyze_permutation_complexity(elements)
        
        for approach, metrics in analysis.items():
            if approach != 'expected_count':
                print(f"{approach.capitalize()}:")
                print(f"  Time: {metrics['time']:.6f}s")
                print(f"  Count: {metrics['count']}")
                print(f"  Correct: {metrics['correct']}")


def demonstrate_memoization_benefits():
    """Demonstrate memoization benefits (if any)."""
    print("\n=== Memoization Benefits ===\n")
    
    elements = [1, 2, 3, 4]
    
    # Test basic backtracking
    start_time = time.time()
    basic_result = permutation_generation_backtracking(elements)
    basic_time = time.time() - start_time
    
    # Test memoized version
    start_time = time.time()
    memo_result = permutation_generation_with_memoization(elements)
    memo_time = time.time() - start_time
    
    print(f"Basic backtracking: {len(basic_result)} permutations (time: {basic_time:.6f}s)")
    print(f"Memoized version: {len(memo_result)} permutations (time: {memo_time:.6f}s)")
    if memo_time > 0:
        print(f"Speedup: {basic_time/memo_time:.2f}x")
    else:
        print("Speedup: N/A (memoized time too small to measure)")
    print(f"Results match: {len(basic_result) == len(memo_result)}")


def demonstrate_counting_functionality():
    """Demonstrate permutation counting functionality."""
    print("\n=== Permutation Counting ===\n")
    
    test_cases = [0, 1, 2, 3, 4, 5, 6]
    
    for n in test_cases:
        count = permutation_generation_count_only(n)
        print(f"{n} elements: {count} permutations ({n}! = {count})")


def demonstrate_practical_applications():
    """Demonstrate practical applications of permutation generation."""
    print("\n=== Practical Applications ===\n")
    
    # Example 1: Arranging books on a shelf
    books = ['Math', 'Physics', 'Chemistry']
    print("Example 1: Arranging books on a shelf")
    print(f"Books: {books}")
    
    arrangements = permutation_generation_backtracking(books)
    print(f"Possible arrangements: {len(arrangements)}")
    for i, arrangement in enumerate(arrangements):
        print(f"  {i+1}. {' -> '.join(arrangement)}")
    
    # Example 2: Scheduling tasks
    tasks = ['Task A', 'Task B', 'Task C']
    print(f"\nExample 2: Scheduling tasks")
    print(f"Tasks: {tasks}")
    
    schedules = permutation_generation_backtracking(tasks)
    print(f"Possible schedules: {len(schedules)}")
    for i, schedule in enumerate(schedules[:3]):  # Show first 3
        print(f"  {i+1}. {' -> '.join(schedule)}")
    if len(schedules) > 3:
        print(f"  ... and {len(schedules) - 3} more")


def demonstrate_complexity_analysis():
    """Demonstrate complexity analysis for different input sizes."""
    print("\n=== Complexity Analysis ===\n")
    
    test_sizes = [1, 2, 3, 4, 5]
    
    print("Input Size | Permutations | Expected")
    print("-" * 35)
    
    for n in test_sizes:
        elements = list(range(1, n + 1))
        count = permutation_generation_count_only(n)
        
        # Time the generation
        start_time = time.time()
        result = permutation_generation_backtracking(elements)
        generation_time = time.time() - start_time
        
        print(f"{n:9d} | {len(result):11d} | {count:9d} ({generation_time:.6f}s)")


def demonstrate_test_cases():
    """Demonstrate the test case creation functionality."""
    print("\n=== Test Cases ===\n")
    
    test_cases = create_test_permutations()
    
    print(f"Generated {len(test_cases)} test cases:")
    for i, test_case in enumerate(test_cases):
        print(f"  {i+1}. {test_case}")
    
    # Test a few cases
    print(f"\nTesting a few cases:")
    for test_case in test_cases[:3]:
        if test_case:
            result = permutation_generation_backtracking(test_case)
            print(f"  {test_case} -> {len(result)} permutations")


if __name__ == "__main__":
    # Run all demonstrations
    demonstrate_basic_functionality()
    demonstrate_duplicate_handling()
    demonstrate_lexicographic_generation()
    demonstrate_constraint_handling()
    demonstrate_performance_comparison()
    demonstrate_memoization_benefits()
    demonstrate_counting_functionality()
    demonstrate_practical_applications()
    demonstrate_complexity_analysis()
    demonstrate_test_cases()
    
    print("\n=== Permutation Generation Demonstration Complete ===") 