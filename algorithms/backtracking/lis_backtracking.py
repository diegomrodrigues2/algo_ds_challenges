"""
Longest Increasing Subsequence (LIS) - Backtracking Implementation

This module implements various backtracking approaches for the Longest Increasing
Subsequence problem, following Erickson's formulation LISbigger(prev, A[j..n]).

The problem: Given a sequence of integers, find the longest subsequence where
each element is greater than the previous one.

Conceptual Link: Erickson, "Algorithms", Chapter 2, Section 2.6, "Longest Increasing Subsequence"
"""

from typing import List, Optional, Tuple, Dict
import time


def lis_backtracking(sequence: List[int]) -> int:
    """
    Basic backtracking implementation for LIS.
    
    Uses Erickson's formulation: LISbigger(prev, A[j..n])
    For each element, decide whether to include it (if A[j] > prev) or skip it.
    
    Args:
        sequence: List of integers
        
    Returns:
        Length of the longest increasing subsequence
        
    Time Complexity: O(2^n) - exponential due to binary decisions
    Space Complexity: O(n) - recursion depth
    """
    if not sequence:
        return 0
    
    def backtrack(index: int, prev: int) -> int:
        if index >= len(sequence):
            return 0
        
        # Skip current element
        skip = backtrack(index + 1, prev)
        
        # Include current element if it's greater than previous
        include = 0
        if sequence[index] > prev:
            include = 1 + backtrack(index + 1, sequence[index])
        
        return max(skip, include)
    
    return backtrack(0, float('-inf'))


def lis_backtracking_with_memoization(sequence: List[int]) -> int:
    """
    Backtracking implementation with memoization to avoid redundant calculations.
    
    Args:
        sequence: List of integers
        
    Returns:
        Length of the longest increasing subsequence
        
    Time Complexity: O(n^2) - memoization reduces exponential complexity
    Space Complexity: O(n^2) - memo table
    """
    if not sequence:
        return 0
    
    memo: Dict[Tuple[int, int], int] = {}
    
    def backtrack(index: int, prev: int) -> int:
        if index >= len(sequence):
            return 0
        
        state = (index, prev)
        if state in memo:
            return memo[state]
        
        # Skip current element
        skip = backtrack(index + 1, prev)
        
        # Include current element if it's greater than previous
        include = 0
        if sequence[index] > prev:
            include = 1 + backtrack(index + 1, sequence[index])
        
        memo[state] = max(skip, include)
        return memo[state]
    
    return backtrack(0, float('-inf'))


def lis_backtracking_all_solutions(sequence: List[int]) -> List[List[int]]:
    """
    Find all longest increasing subsequences.
    
    Args:
        sequence: List of integers
        
    Returns:
        List of all longest increasing subsequences
        
    Time Complexity: O(2^n) - exponential
    Space Complexity: O(n * 2^n) - storing all solutions
    """
    if not sequence:
        return []
    
    max_length = 0
    all_solutions: List[List[int]] = []
    
    def backtrack(index: int, prev: int, current: List[int]) -> None:
        nonlocal max_length
        
        if index >= len(sequence):
            if len(current) > max_length:
                max_length = len(current)
                all_solutions.clear()
                all_solutions.append(current[:])
            elif len(current) == max_length:
                all_solutions.append(current[:])
            return
        
        # Skip current element
        backtrack(index + 1, prev, current)
        
        # Include current element if it's greater than previous
        if sequence[index] > prev:
            current.append(sequence[index])
            backtrack(index + 1, sequence[index], current)
            current.pop()
    
    backtrack(0, float('-inf'), [])
    return all_solutions


def lis_backtracking_count_solutions(sequence: List[int]) -> Tuple[int, int]:
    """
    Count the number of longest increasing subsequences.
    
    Args:
        sequence: List of integers
        
    Returns:
        Tuple of (length of LIS, number of LIS with that length)
        
    Time Complexity: O(2^n) - exponential
    Space Complexity: O(n) - recursion depth
    """
    if not sequence:
        return (0, 0)
    
    max_length = 0
    count = 0
    
    def backtrack(index: int, prev: int, current_length: int) -> None:
        nonlocal max_length, count
        
        if index >= len(sequence):
            if current_length > max_length:
                max_length = current_length
                count = 1
            elif current_length == max_length:
                count += 1
            return
        
        # Skip current element
        backtrack(index + 1, prev, current_length)
        
        # Include current element if it's greater than previous
        if sequence[index] > prev:
            backtrack(index + 1, sequence[index], current_length + 1)
    
    backtrack(0, float('-inf'), 0)
    return (max_length, count)


def lis_backtracking_optimized(sequence: List[int]) -> int:
    """
    Optimized backtracking with early termination and better pruning.
    
    Args:
        sequence: List of integers
        
    Returns:
        Length of the longest increasing subsequence
        
    Time Complexity: O(2^n) - but with better pruning
    Space Complexity: O(n) - recursion depth
    """
    if not sequence:
        return 0
    
    n = len(sequence)
    best_length = 0
    
    def backtrack(index: int, prev: int, current_length: int) -> None:
        nonlocal best_length
        
        # Early termination: if remaining elements + current length <= best
        remaining = n - index
        if current_length + remaining <= best_length:
            return
        
        if index >= n:
            best_length = max(best_length, current_length)
            return
        
        # Skip current element
        backtrack(index + 1, prev, current_length)
        
        # Include current element if it's greater than previous
        if sequence[index] > prev:
            backtrack(index + 1, sequence[index], current_length + 1)
    
    backtrack(0, float('-inf'), 0)
    return best_length


def analyze_lis_complexity(sequence: List[int]) -> Dict[str, any]:
    """
    Analyze the complexity and performance of different LIS implementations.
    
    Args:
        sequence: List of integers to analyze
        
    Returns:
        Dictionary with analysis results
    """
    results = {}
    
    # Test basic backtracking
    start_time = time.time()
    basic_result = lis_backtracking(sequence)
    basic_time = time.time() - start_time
    
    # Test memoized version
    start_time = time.time()
    memo_result = lis_backtracking_with_memoization(sequence)
    memo_time = time.time() - start_time
    
    # Test optimized version
    start_time = time.time()
    optimized_result = lis_backtracking_optimized(sequence)
    optimized_time = time.time() - start_time
    
    # Count solutions
    start_time = time.time()
    length, count = lis_backtracking_count_solutions(sequence)
    count_time = time.time() - start_time
    
    results = {
        'sequence_length': len(sequence),
        'basic_backtracking': {
            'result': basic_result,
            'time': basic_time,
            'complexity': 'O(2^n)'
        },
        'memoized': {
            'result': memo_result,
            'time': memo_time,
            'complexity': 'O(n^2)'
        },
        'optimized': {
            'result': optimized_result,
            'time': optimized_time,
            'complexity': 'O(2^n) with pruning'
        },
        'count_analysis': {
            'length': length,
            'count': count,
            'time': count_time
        },
        'correctness': {
            'all_equal': basic_result == memo_result == optimized_result,
            'basic_memo_equal': basic_result == memo_result,
            'basic_optimized_equal': basic_result == optimized_result
        }
    }
    
    return results


def lis_backtracking_with_path(sequence: List[int]) -> Tuple[int, List[int]]:
    """
    Find the length and one example of the longest increasing subsequence.
    
    Args:
        sequence: List of integers
        
    Returns:
        Tuple of (length of LIS, one example LIS)
        
    Time Complexity: O(2^n) - exponential
    Space Complexity: O(n) - recursion depth
    """
    if not sequence:
        return (0, [])
    
    best_length = 0
    best_path = []
    
    def backtrack(index: int, prev: int, current: List[int]) -> None:
        nonlocal best_length, best_path
        
        if index >= len(sequence):
            if len(current) > best_length:
                best_length = len(current)
                best_path = current[:]
            return
        
        # Skip current element
        backtrack(index + 1, prev, current)
        
        # Include current element if it's greater than previous
        if sequence[index] > prev:
            current.append(sequence[index])
            backtrack(index + 1, sequence[index], current)
            current.pop()
    
    backtrack(0, float('-inf'), [])
    return (best_length, best_path)


def lis_backtracking_erickson_formulation(sequence: List[int]) -> int:
    """
    Direct implementation of Erickson's LISbigger(prev, A[j..n]) formulation.
    
    This is the most direct translation of Erickson's recursive formulation:
    LISbigger(prev, A[j..n]) = max(
        LISbigger(prev, A[j+1..n]),           # skip A[j]
        1 + LISbigger(A[j], A[j+1..n])        # include A[j] if A[j] > prev
    )
    
    Args:
        sequence: List of integers
        
    Returns:
        Length of the longest increasing subsequence
        
    Time Complexity: O(2^n) - exponential
    Space Complexity: O(n) - recursion depth
    """
    if not sequence:
        return 0
    
    def lis_bigger(prev: int, start: int) -> int:
        """
        Erickson's LISbigger(prev, A[start..n]) formulation.
        
        Args:
            prev: Previous element in the subsequence
            start: Starting index in the sequence
            
        Returns:
            Length of LIS starting from index 'start' with elements > prev
        """
        if start >= len(sequence):
            return 0
        
        # Skip current element: LISbigger(prev, A[start+1..n])
        skip = lis_bigger(prev, start + 1)
        
        # Include current element if it's greater than prev
        include = 0
        if sequence[start] > prev:
            include = 1 + lis_bigger(sequence[start], start + 1)
        
        return max(skip, include)
    
    return lis_bigger(float('-inf'), 0)


def lis_backtracking_erickson_memoized(sequence: List[int]) -> int:
    """
    Erickson's formulation with memoization.
    
    Args:
        sequence: List of integers
        
    Returns:
        Length of the longest increasing subsequence
        
    Time Complexity: O(n^2) - memoization reduces exponential complexity
    Space Complexity: O(n^2) - memo table
    """
    if not sequence:
        return 0
    
    memo: Dict[Tuple[int, int], int] = {}
    
    def lis_bigger(prev: int, start: int) -> int:
        if start >= len(sequence):
            return 0
        
        state = (prev, start)
        if state in memo:
            return memo[state]
        
        # Skip current element
        skip = lis_bigger(prev, start + 1)
        
        # Include current element if it's greater than prev
        include = 0
        if sequence[start] > prev:
            include = 1 + lis_bigger(sequence[start], start + 1)
        
        memo[state] = max(skip, include)
        return memo[state]
    
    return lis_bigger(float('-inf'), 0)


# Helper function for testing
def create_test_sequences() -> List[List[int]]:
    """Create various test sequences for LIS testing."""
    return [
        [],  # Empty sequence
        [1],  # Single element
        [1, 2, 3, 4, 5],  # Strictly increasing
        [5, 4, 3, 2, 1],  # Strictly decreasing
        [1, 3, 2, 4, 5],  # Mixed
        [10, 22, 9, 33, 21, 50, 41, 60],  # Classic example
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],  # Complex example
        [1, 1, 1, 1, 1],  # All same elements
        [1, 2, 1, 2, 1, 2],  # Alternating
        [1, 2, 3, 1, 2, 3, 1, 2, 3],  # Repeating pattern
    ] 