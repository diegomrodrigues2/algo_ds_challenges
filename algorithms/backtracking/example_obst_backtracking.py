"""
Example usage of Optimal Binary Search Tree (OBST) Backtracking Implementation

This script demonstrates the various OBST backtracking functions with different
examples and shows the performance differences between implementations.
"""

import time
from obst_backtracking import (
    obst_backtracking,
    obst_backtracking_with_memoization,
    obst_backtracking_with_structure,
    obst_backtracking_all_structures,
    obst_backtracking_count_structures,
    obst_backtracking_optimized,
    analyze_obst_complexity,
    obst_backtracking_with_tree_building,
    obst_backtracking_erickson_formulation,
    obst_backtracking_erickson_memoized,
    create_test_obst_cases
)


def demonstrate_basic_functionality():
    """Demonstrate basic OBST backtracking functionality."""
    print("=== Basic OBST Backtracking Functionality ===")
    
    # Test cases
    test_cases = [
        ([], [], "Empty case"),
        ([1], [10], "Single key"),
        ([1, 2], [34, 50], "Two keys"),
        ([10, 12, 20], [34, 8, 50], "Three keys - Classic example"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "Sequential keys"),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], "Reverse frequencies"),
    ]
    
    for keys, freq, description in test_cases:
        result = obst_backtracking(keys, freq)
        print(f"{description}: keys={keys}, freq={freq} -> Cost: {result}")


def demonstrate_memoization_benefits():
    """Demonstrate the benefits of memoization."""
    print("\n=== Memoization Benefits ===")
    
    # Use a larger input to show performance difference
    keys = [1, 2, 3, 4, 5, 6, 7]
    freq = [1, 2, 3, 4, 3, 2, 1]
    
    print(f"Testing keys: {keys}")
    print(f"Frequencies: {freq}")
    print(f"Number of keys: {len(keys)}")
    
    # Test basic backtracking
    start_time = time.time()
    basic_result = obst_backtracking(keys, freq)
    basic_time = time.time() - start_time
    
    # Test memoized version
    start_time = time.time()
    memo_result = obst_backtracking_with_memoization(keys, freq)
    memo_time = time.time() - start_time
    
    print(f"Basic backtracking: {basic_result} (time: {basic_time:.6f}s)")
    print(f"Memoized version: {memo_result} (time: {memo_time:.6f}s)")
    if memo_time > 0:
        print(f"Speedup: {basic_time/memo_time:.2f}x")
    else:
        print("Speedup: N/A (memoized time too small to measure)")
    print(f"Results match: {basic_result == memo_result}")


def demonstrate_structure_building():
    """Demonstrate finding optimal tree structure."""
    print("\n=== Finding Optimal Tree Structure ===")
    
    test_cases = [
        ([1, 2], [34, 50], "Two keys"),
        ([10, 12, 20], [34, 8, 50], "Three keys"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "Sequential"),
    ]
    
    for keys, freq, description in test_cases:
        cost, structure = obst_backtracking_with_structure(keys, freq)
        print(f"{description}: keys={keys}, freq={freq}")
        print(f"  Optimal cost: {cost}")
        print(f"  Root structure: {structure}")
        
        # Show which key is chosen as root for each range
        for (i, j), root_idx in structure.items():
            if i <= root_idx <= j:
                print(f"    Range [{i},{j}] -> Root: key {keys[root_idx]} (index {root_idx})")
        print()


def demonstrate_tree_building():
    """Demonstrate building the actual tree structure."""
    print("\n=== Building Tree Structure ===")
    
    test_cases = [
        ([1, 2], [34, 50], "Two keys"),
        ([10, 12, 20], [34, 8, 50], "Three keys"),
    ]
    
    for keys, freq, description in test_cases:
        cost, tree = obst_backtracking_with_tree_building(keys, freq)
        print(f"{description}: keys={keys}, freq={freq}")
        print(f"  Optimal cost: {cost}")
        print(f"  Tree structure: {tree}")
        
        # Show the tree structure
        for key, (left, right) in tree.items():
            left_key = keys[left] if left >= 0 else "None"
            right_key = keys[right] if right >= 0 else "None"
            print(f"    Key {key}: left={left_key}, right={right_key}")
        print()


def demonstrate_counting_structures():
    """Demonstrate counting optimal structures."""
    print("\n=== Counting Optimal Structures ===")
    
    test_cases = [
        ([1, 2], [34, 50], "Two keys"),
        ([10, 12, 20], [34, 8, 50], "Three keys"),
        ([1, 2, 3], [1, 1, 1], "Equal frequencies"),
    ]
    
    for keys, freq, description in test_cases:
        cost, count = obst_backtracking_count_structures(keys, freq)
        print(f"{description}: keys={keys}, freq={freq}")
        print(f"  Optimal cost: {cost}")
        print(f"  Number of optimal structures: {count}")
        print()


def demonstrate_all_structures():
    """Demonstrate finding all optimal structures."""
    print("\n=== Finding All Optimal Structures ===")
    
    test_cases = [
        ([1, 2], [34, 50], "Two keys"),
        ([1, 2, 3], [1, 1, 1], "Equal frequencies"),
    ]
    
    for keys, freq, description in test_cases:
        structures = obst_backtracking_all_structures(keys, freq)
        print(f"{description}: keys={keys}, freq={freq}")
        print(f"  Number of optimal structures: {len(structures)}")
        
        for i, structure in enumerate(structures[:3]):  # Show first 3 structures
            print(f"    Structure {i+1}: {structure}")
        if len(structures) > 3:
            print(f"    ... and {len(structures) - 3} more structures")
        print()


def demonstrate_erickson_formulation():
    """Demonstrate Erickson's formulation."""
    print("\n=== Erickson's OptCost Formulation ===")
    
    test_cases = [
        ([1, 2], [34, 50], "Two keys"),
        ([10, 12, 20], [34, 8, 50], "Three keys"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "Sequential"),
    ]
    
    for keys, freq, description in test_cases:
        basic_result = obst_backtracking(keys, freq)
        erickson_result = obst_backtracking_erickson_formulation(keys, freq)
        erickson_memo_result = obst_backtracking_erickson_memoized(keys, freq)
        
        print(f"{description}: keys={keys}, freq={freq}")
        print(f"  Basic backtracking: {basic_result}")
        print(f"  Erickson formulation: {erickson_result}")
        print(f"  Erickson memoized: {erickson_memo_result}")
        print(f"  All match: {basic_result == erickson_result == erickson_memo_result}")
        print()


def demonstrate_complexity_analysis():
    """Demonstrate complexity analysis."""
    print("\n=== Complexity Analysis ===")
    
    # Test with different input sizes
    test_cases = [
        ([1, 2, 3], [1, 2, 3], "Small"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "Medium"),
    ]
    
    for keys, freq, description in test_cases:
        print(f"Analyzing {description}: keys={keys}, freq={freq}")
        analysis = analyze_obst_complexity(keys, freq)
        
        print(f"  Number of keys: {analysis['keys_length']}")
        print(f"  Basic backtracking: {analysis['basic_backtracking']['result']} "
              f"({analysis['basic_backtracking']['time']:.6f}s)")
        print(f"  Memoized: {analysis['memoized']['result']} "
              f"({analysis['memoized']['time']:.6f}s)")
        print(f"  Optimized: {analysis['optimized']['result']} "
              f"({analysis['optimized']['time']:.6f}s)")
        print(f"  Structure analysis: {analysis['structure_analysis']['cost']} cost, "
              f"{analysis['structure_analysis']['count']} structures")
        print(f"  All results match: {analysis['correctness']['all_equal']}")
        print()


def demonstrate_test_cases():
    """Demonstrate the test cases helper function."""
    print("\n=== Test Cases ===")
    
    cases = create_test_obst_cases()
    print(f"Number of test cases: {len(cases)}")
    
    for i, (keys, freq) in enumerate(cases):
        if len(keys) <= 5:  # Limit size for exponential algorithms
            result = obst_backtracking(keys, freq)
            print(f"  Case {i+1}: keys={keys}, freq={freq} -> Cost: {result}")


def demonstrate_classic_example():
    """Demonstrate the classic OBST example from GeeksforGeeks."""
    print("\n=== Classic OBST Example ===")
    
    # Example from GeeksforGeeks
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    
    print(f"Keys: {keys}")
    print(f"Frequencies: {freq}")
    
    # Calculate costs for different tree structures
    print("\nPossible tree structures:")
    
    # Tree 1: 10 as root
    #    10
    #      \
    #       12
    #         \
    #          20
    cost1 = 34*1 + 8*2 + 50*3  # 34 + 16 + 150 = 200
    print(f"  Tree 1 (10 as root): Cost = {cost1}")
    
    # Tree 2: 12 as root
    #    12
    #   /  \
    #  10   20
    cost2 = 8*1 + 34*2 + 50*2  # 8 + 68 + 100 = 176
    print(f"  Tree 2 (12 as root): Cost = {cost2}")
    
    # Tree 3: 20 as root
    #    20
    #   /
    #  12
    # /
    #10
    cost3 = 50*1 + 8*2 + 34*3  # 50 + 16 + 102 = 168
    print(f"  Tree 3 (20 as root): Cost = {cost3}")
    
    # Find optimal using our algorithm
    optimal_cost = obst_backtracking(keys, freq)
    print(f"\nOptimal cost (algorithm): {optimal_cost}")
    print(f"Best manual structure: Tree 3 with cost {cost3}")
    print(f"Algorithm matches manual: {optimal_cost == cost3}")


def main():
    """Main demonstration function."""
    print("Optimal Binary Search Tree (OBST) Backtracking Demonstration")
    print("=" * 60)
    
    try:
        demonstrate_basic_functionality()
        demonstrate_memoization_benefits()
        demonstrate_structure_building()
        demonstrate_tree_building()
        demonstrate_counting_structures()
        demonstrate_all_structures()
        demonstrate_erickson_formulation()
        demonstrate_complexity_analysis()
        demonstrate_test_cases()
        demonstrate_classic_example()
        
        print("\n=== All Demonstrations Completed Successfully ===")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 