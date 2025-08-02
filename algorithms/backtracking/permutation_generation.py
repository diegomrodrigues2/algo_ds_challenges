"""
Permutation Generation (Geração de Permutações)

This module implements various backtracking approaches for generating all permutations
of a given set of elements. The problem is a classic backtracking challenge where
at each recursive step, an unused element is chosen.

Key Concepts:
- Binary decision tree structure (include/exclude for each position)
- In-place swapping approach for efficiency
- Remaining elements approach for clarity
- Lexicographic ordering
- Handling duplicates

References:
- Erickson, "Algorithms", Chapter 2, Section 2.4 (Backtracking)
- GeeksforGeeks: Print all permutations of a given string
- GeeksforGeeks: Generate all the permutation of a list in Python
"""

from typing import List, Set, Optional, Callable
import time
from collections import Counter


def permutation_generation_backtracking(elements: List) -> List[List]:
    """
    Generate all permutations using backtracking with remaining elements approach.
    
    This approach maintains a list of remaining elements and chooses one at each step.
    
    Args:
        elements: List of elements to permute
        
    Returns:
        List of all possible permutations
        
    Time Complexity: O(n!)
    Space Complexity: O(n) for recursion + O(n!) for result
    """
    if not elements:
        return [[]]
    
    result = []
    
    def backtrack(remaining: List, current: List) -> None:
        if not remaining:
            result.append(current[:])
            return
        
        for i in range(len(remaining)):
            # Choose element at position i
            chosen = remaining[i]
            current.append(chosen)
            
            # Remove chosen element from remaining
            new_remaining = remaining[:i] + remaining[i+1:]
            
            # Recurse with remaining elements
            backtrack(new_remaining, current)
            
            # Backtrack
            current.pop()
    
    backtrack(elements, [])
    return result


def permutation_generation_inplace_swap(elements: List) -> List[List]:
    """
    Generate all permutations using in-place swapping approach.
    
    This approach modifies the original array by swapping elements and then
    reverting the changes (backtracking).
    
    Args:
        elements: List of elements to permute
        
    Returns:
        List of all possible permutations
        
    Time Complexity: O(n!)
    Space Complexity: O(n) for recursion + O(n!) for result
    """
    if not elements:
        return [[]]
    
    result = []
    elements_copy = elements[:]  # Work on a copy to preserve original
    
    def backtrack(start: int) -> None:
        if start == len(elements_copy):
            result.append(elements_copy[:])
            return
        
        for i in range(start, len(elements_copy)):
            # Swap current position with position i
            elements_copy[start], elements_copy[i] = elements_copy[i], elements_copy[start]
            
            # Recurse on next position
            backtrack(start + 1)
            
            # Backtrack: swap back
            elements_copy[start], elements_copy[i] = elements_copy[i], elements_copy[start]
    
    backtrack(0)
    return result


def permutation_generation_with_duplicates(elements: List) -> List[List]:
    """
    Generate all unique permutations when input contains duplicates.
    
    Uses a frequency counter to avoid generating duplicate permutations.
    
    Args:
        elements: List of elements (may contain duplicates)
        
    Returns:
        List of all unique permutations
        
    Time Complexity: O(n!)
    Space Complexity: O(n) for recursion + O(n!) for result
    """
    if not elements:
        return [[]]
    
    result = []
    freq = Counter(elements)
    
    def backtrack(current: List) -> None:
        if len(current) == len(elements):
            result.append(current[:])
            return
        
        for num in freq:
            if freq[num] > 0:
                # Use this number
                freq[num] -= 1
                current.append(num)
                
                backtrack(current)
                
                # Backtrack
                current.pop()
                freq[num] += 1
    
    backtrack([])
    return result


def permutation_generation_lexicographic(elements: List) -> List[List]:
    """
    Generate permutations in lexicographic order.
    
    Uses the next permutation algorithm to generate permutations in order.
    
    Args:
        elements: List of elements to permute
        
    Returns:
        List of all permutations in lexicographic order
        
    Time Complexity: O(n!)
    Space Complexity: O(n) for recursion + O(n!) for result
    """
    if not elements:
        return [[]]
    
    result = []
    elements_copy = sorted(elements[:])  # Start with sorted array
    
    def next_permutation() -> bool:
        """Find next permutation in lexicographic order."""
        n = len(elements_copy)
        
        # Find the largest index k such that a[k] < a[k + 1]
        k = n - 2
        while k >= 0 and elements_copy[k] >= elements_copy[k + 1]:
            k -= 1
        
        if k < 0:
            return False  # No more permutations
        
        # Find the largest index l such that a[k] < a[l]
        l = n - 1
        while elements_copy[k] >= elements_copy[l]:
            l -= 1
        
        # Swap a[k] and a[l]
        elements_copy[k], elements_copy[l] = elements_copy[l], elements_copy[k]
        
        # Reverse the sequence from a[k + 1] to a[n - 1]
        left = k + 1
        right = n - 1
        while left < right:
            elements_copy[left], elements_copy[right] = elements_copy[right], elements_copy[left]
            left += 1
            right -= 1
        
        return True
    
    # Add first permutation
    result.append(elements_copy[:])
    
    # Generate all subsequent permutations
    while next_permutation():
        result.append(elements_copy[:])
    
    return result


def permutation_generation_count_only(n: int) -> int:
    """
    Count the number of permutations without generating them.
    
    Args:
        n: Number of elements
        
    Returns:
        Number of possible permutations (n!)
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def permutation_generation_with_constraints(elements: List, 
                                         constraint_func: Callable[[List], bool]) -> List[List]:
    """
    Generate permutations that satisfy a given constraint.
    
    Args:
        elements: List of elements to permute
        constraint_func: Function that takes a partial permutation and returns True
                       if it can be extended to a valid solution
        
    Returns:
        List of all valid permutations
        
    Time Complexity: O(n!)
    Space Complexity: O(n) for recursion + O(n!) for result
    """
    if not elements:
        return [[]]
    
    result = []
    
    def backtrack(remaining: List, current: List) -> None:
        if not remaining:
            result.append(current[:])
            return
        
        for i in range(len(remaining)):
            chosen = remaining[i]
            current.append(chosen)
            
            # Check if current partial solution can be extended
            if constraint_func(current):
                new_remaining = remaining[:i] + remaining[i+1:]
                backtrack(new_remaining, current)
            
            current.pop()
    
    backtrack(elements, [])
    return result


def permutation_generation_optimized(elements: List) -> List[List]:
    """
    Optimized permutation generation with minimal allocations.
    
    Args:
        elements: List of elements to permute
        
    Returns:
        List of all possible permutations
        
    Time Complexity: O(n!)
    Space Complexity: O(n) for recursion + O(n!) for result
    """
    if not elements:
        return [[]]
    
    result = []
    n = len(elements)
    used = [False] * n
    current = [0] * n
    
    def backtrack(pos: int) -> None:
        if pos == n:
            # Convert indices to actual elements
            permutation = [elements[i] for i in current]
            result.append(permutation)
            return
        
        for i in range(n):
            if not used[i]:
                used[i] = True
                current[pos] = i
                backtrack(pos + 1)
                used[i] = False
    
    backtrack(0)
    return result


def permutation_generation_with_memoization(elements: List) -> List[List]:
    """
    Permutation generation with memoization (demonstrates concept).
    
    Note: For permutation generation, memoization doesn't provide significant
    benefits since each path is unique, but it demonstrates the concept.
    
    Args:
        elements: List of elements to permute
        
    Returns:
        List of all possible permutations
        
    Time Complexity: O(n!)
    Space Complexity: O(n) for recursion + O(n!) for result + O(n!) for memo
    """
    if not elements:
        return [[]]
    
    result = []
    memo = {}
    
    def backtrack(remaining: List, current: List) -> None:
        # Create a key for memoization
        remaining_key = tuple(sorted(remaining))
        current_key = tuple(current)
        key = (remaining_key, current_key)
        
        if key in memo:
            return
        
        if not remaining:
            result.append(current[:])
            memo[key] = True
            return
        
        for i in range(len(remaining)):
            chosen = remaining[i]
            current.append(chosen)
            
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(new_remaining, current)
            
            current.pop()
        
        memo[key] = True
    
    backtrack(elements, [])
    return result


def analyze_permutation_complexity(elements: List) -> dict:
    """
    Analyze the complexity and performance of different permutation generation approaches.
    
    Args:
        elements: List of elements to test
        
    Returns:
        Dictionary with performance metrics
    """
    results = {}
    
    # Test backtracking approach
    start_time = time.time()
    backtrack_result = permutation_generation_backtracking(elements)
    backtrack_time = time.time() - start_time
    
    # Test in-place swap approach
    start_time = time.time()
    swap_result = permutation_generation_inplace_swap(elements)
    swap_time = time.time() - start_time
    
    # Test optimized approach
    start_time = time.time()
    optimized_result = permutation_generation_optimized(elements)
    optimized_time = time.time() - start_time
    
    # Test lexicographic approach
    start_time = time.time()
    lex_result = permutation_generation_lexicographic(elements)
    lex_time = time.time() - start_time
    
    results = {
        'backtracking': {
            'time': backtrack_time,
            'count': len(backtrack_result),
            'correct': len(backtrack_result) == permutation_generation_count_only(len(elements))
        },
        'inplace_swap': {
            'time': swap_time,
            'count': len(swap_result),
            'correct': len(swap_result) == permutation_generation_count_only(len(elements))
        },
        'optimized': {
            'time': optimized_time,
            'count': len(optimized_result),
            'correct': len(optimized_result) == permutation_generation_count_only(len(elements))
        },
        'lexicographic': {
            'time': lex_time,
            'count': len(lex_result),
            'correct': len(lex_result) == permutation_generation_count_only(len(elements))
        },
        'expected_count': permutation_generation_count_only(len(elements))
    }
    
    return results


def create_test_permutations() -> List[List]:
    """
    Create test cases for permutation generation.
    
    Returns:
        List of test cases
    """
    return [
        [],  # Empty list
        [1],  # Single element
        [1, 2],  # Two elements
        [1, 2, 3],  # Three elements
        [1, 1, 2],  # With duplicates
        ['a', 'b', 'c'],  # Strings
        [1, 2, 3, 4],  # Four elements
        [1, 1, 1, 1],  # All duplicates
    ]


def demonstrate_permutation_generation():
    """
    Demonstrate the permutation generation functionality.
    """
    print("=== Permutation Generation Demonstration ===\n")
    
    # Test basic functionality
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
        all_same = (len(backtrack_result) == len(swap_result == len(optimized_result)))
        print(f"All approaches consistent: {all_same}")
        
        if elements:
            print(f"Sample permutation: {backtrack_result[0] if backtrack_result else 'N/A'}")


def demonstrate_duplicate_handling():
    """
    Demonstrate handling of duplicate elements.
    """
    print("\n=== Duplicate Handling Demonstration ===\n")
    
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


def demonstrate_performance_comparison():
    """
    Demonstrate performance comparison between different approaches.
    """
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


def demonstrate_constraint_handling():
    """
    Demonstrate constraint-based permutation generation.
    """
    print("\n=== Constraint Handling Demonstration ===\n")
    
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


if __name__ == "__main__":
    # Run demonstrations
    demonstrate_permutation_generation()
    demonstrate_duplicate_handling()
    demonstrate_performance_comparison()
    demonstrate_constraint_handling() 