"""
Optimal Binary Search Tree (OBST) - Backtracking Implementation

This module implements various backtracking approaches for the Optimal Binary
Search Tree problem, following Erickson's OptCost(i, k) formulation.

The problem: Given a sorted array of keys and their frequencies, construct
a binary search tree that minimizes the total cost of all searches.

Conceptual Link: Erickson, "Algorithms", Chapter 2, Section 2.8, "Optimal Binary Search Trees"
"""

from typing import List, Optional, Tuple, Dict
import time


def obst_backtracking(keys: List[int], freq: List[int]) -> int:
    """
    Basic backtracking implementation for Optimal Binary Search Tree.
    
    Uses Erickson's formulation: OptCost(i, k) = min(OptCost(i, r-1) + OptCost(r+1, k) + fsum)
    For each possible root r in [i, k], calculate the cost and choose the minimum.
    
    Args:
        keys: Sorted array of search keys
        freq: Frequency counts for each key
        
    Returns:
        Minimum cost of the optimal binary search tree
        
    Time Complexity: O(n * 2^n) - exponential due to testing all possible roots
    Space Complexity: O(n) - recursion depth
    """
    if not keys or not freq or len(keys) != len(freq):
        return 0
    
    def sum_freq(i: int, j: int) -> int:
        """Calculate sum of frequencies from index i to j."""
        return sum(freq[i:j+1])
    
    def opt_cost(i: int, j: int) -> int:
        if i > j:
            return 0  # No nodes in this subarray
        if i == j:
            return freq[i]  # Only one node
        
        # Get sum of frequencies for this range
        fsum = sum_freq(i, j)
        
        # Try each key as root and find minimum cost
        min_cost = float('inf')
        for r in range(i, j + 1):
            cost = opt_cost(i, r - 1) + opt_cost(r + 1, j)
            if cost < min_cost:
                min_cost = cost
        
        return min_cost + fsum
    
    return opt_cost(0, len(keys) - 1)


def obst_backtracking_with_memoization(keys: List[int], freq: List[int]) -> int:
    """
    Backtracking implementation with memoization to avoid redundant calculations.
    
    Args:
        keys: Sorted array of search keys
        freq: Frequency counts for each key
        
    Returns:
        Minimum cost of the optimal binary search tree
        
    Time Complexity: O(n³) - memoization reduces exponential complexity
    Space Complexity: O(n²) - memo table
    """
    if not keys or not freq or len(keys) != len(freq):
        return 0
    
    memo: Dict[Tuple[int, int], int] = {}
    
    def sum_freq(i: int, j: int) -> int:
        """Calculate sum of frequencies from index i to j."""
        return sum(freq[i:j+1])
    
    def opt_cost(i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return freq[i]
        
        state = (i, j)
        if state in memo:
            return memo[state]
        
        # Get sum of frequencies for this range
        fsum = sum_freq(i, j)
        
        # Try each key as root and find minimum cost
        min_cost = float('inf')
        for r in range(i, j + 1):
            cost = opt_cost(i, r - 1) + opt_cost(r + 1, j)
            if cost < min_cost:
                min_cost = cost
        
        memo[state] = min_cost + fsum
        return memo[state]
    
    return opt_cost(0, len(keys) - 1)


def obst_backtracking_with_structure(keys: List[int], freq: List[int]) -> Tuple[int, Dict[Tuple[int, int], int]]:
    """
    Find the optimal cost and the root structure of the OBST.
    
    Args:
        keys: Sorted array of search keys
        freq: Frequency counts for each key
        
    Returns:
        Tuple of (minimum cost, root structure dictionary)
        
    Time Complexity: O(n³) with memoization
    Space Complexity: O(n²) - memo table + root structure
    """
    if not keys or not freq or len(keys) != len(freq):
        return (0, {})
    
    memo: Dict[Tuple[int, int], int] = {}
    root_structure: Dict[Tuple[int, int], int] = {}
    
    def sum_freq(i: int, j: int) -> int:
        """Calculate sum of frequencies from index i to j."""
        return sum(freq[i:j+1])
    
    def opt_cost(i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return freq[i]
        
        state = (i, j)
        if state in memo:
            return memo[state]
        
        # Get sum of frequencies for this range
        fsum = sum_freq(i, j)
        
        # Try each key as root and find minimum cost
        min_cost = float('inf')
        best_root = i
        
        for r in range(i, j + 1):
            cost = opt_cost(i, r - 1) + opt_cost(r + 1, j)
            if cost < min_cost:
                min_cost = cost
                best_root = r
        
        memo[state] = min_cost + fsum
        root_structure[state] = best_root
        return memo[state]
    
    result = opt_cost(0, len(keys) - 1)
    return (result, root_structure)


def obst_backtracking_all_structures(keys: List[int], freq: List[int]) -> List[Dict[Tuple[int, int], int]]:
    """
    Find all possible optimal structures (when there are ties).
    
    Args:
        keys: Sorted array of search keys
        freq: Frequency counts for each key
        
    Returns:
        List of all optimal root structures
        
    Time Complexity: O(n³ * k) where k is number of optimal structures
    Space Complexity: O(n² * k)
    """
    if not keys or not freq or len(keys) != len(freq):
        return []
    
    memo: Dict[Tuple[int, int], int] = {}
    all_structures: List[Dict[Tuple[int, int], int]] = []
    min_cost = float('inf')
    
    def sum_freq(i: int, j: int) -> int:
        """Calculate sum of frequencies from index i to j."""
        return sum(freq[i:j+1])
    
    def opt_cost(i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return freq[i]
        
        state = (i, j)
        if state in memo:
            return memo[state]
        
        # Get sum of frequencies for this range
        fsum = sum_freq(i, j)
        
        # Try each key as root and find minimum cost
        min_cost_local = float('inf')
        for r in range(i, j + 1):
            cost = opt_cost(i, r - 1) + opt_cost(r + 1, j)
            if cost < min_cost_local:
                min_cost_local = cost
        
        memo[state] = min_cost_local + fsum
        return memo[state]
    
    def find_structures(i: int, j: int, current_structure: Dict[Tuple[int, int], int]) -> None:
        """Find all optimal structures recursively."""
        if i > j:
            return
        
        if i == j:
            current_structure[(i, j)] = i
            return
        
        # Get optimal cost for this range
        optimal_cost = opt_cost(i, j)
        fsum = sum_freq(i, j)
        
        # Find all roots that give the optimal cost
        for r in range(i, j + 1):
            cost = opt_cost(i, r - 1) + opt_cost(r + 1, j)
            if cost + fsum == optimal_cost:
                # This root gives optimal cost
                new_structure = current_structure.copy()
                new_structure[(i, j)] = r
                
                # Recursively find structures for left and right subtrees
                find_structures(i, r - 1, new_structure)
                find_structures(r + 1, j, new_structure)
                
                # If this is a complete structure, add it
                if len(new_structure) == len(keys):
                    all_structures.append(new_structure)
    
    # Find the minimum cost first
    min_cost = opt_cost(0, len(keys) - 1)
    
    # Find all optimal structures
    find_structures(0, len(keys) - 1, {})
    
    return all_structures


def obst_backtracking_count_structures(keys: List[int], freq: List[int]) -> Tuple[int, int]:
    """
    Count the number of optimal binary search tree structures.
    
    Args:
        keys: Sorted array of search keys
        freq: Frequency counts for each key
        
    Returns:
        Tuple of (minimum cost, number of optimal structures)
        
    Time Complexity: O(n³)
    Space Complexity: O(n²)
    """
    if not keys or not freq or len(keys) != len(freq):
        return (0, 0)
    
    memo: Dict[Tuple[int, int], int] = {}
    count_memo: Dict[Tuple[int, int], int] = {}
    
    def sum_freq(i: int, j: int) -> int:
        """Calculate sum of frequencies from index i to j."""
        return sum(freq[i:j+1])
    
    def opt_cost(i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return freq[i]
        
        state = (i, j)
        if state in memo:
            return memo[state]
        
        # Get sum of frequencies for this range
        fsum = sum_freq(i, j)
        
        # Try each key as root and find minimum cost
        min_cost = float('inf')
        for r in range(i, j + 1):
            cost = opt_cost(i, r - 1) + opt_cost(r + 1, j)
            if cost < min_cost:
                min_cost = cost
        
        memo[state] = min_cost + fsum
        return memo[state]
    
    def count_structures(i: int, j: int) -> int:
        """Count number of optimal structures for range [i, j]."""
        if i > j:
            return 1  # One way to represent empty subtree
        if i == j:
            return 1  # One way to represent single node
        
        state = (i, j)
        if state in count_memo:
            return count_memo[state]
        
        # Get optimal cost for this range
        optimal_cost = opt_cost(i, j)
        fsum = sum_freq(i, j)
        
        # Count all roots that give the optimal cost
        count = 0
        for r in range(i, j + 1):
            cost = opt_cost(i, r - 1) + opt_cost(r + 1, j)
            if cost + fsum == optimal_cost:
                # This root gives optimal cost
                left_count = count_structures(i, r - 1)
                right_count = count_structures(r + 1, j)
                count += left_count * right_count
        
        count_memo[state] = count
        return count
    
    min_cost = opt_cost(0, len(keys) - 1)
    structure_count = count_structures(0, len(keys) - 1)
    
    return (min_cost, structure_count)


def obst_backtracking_optimized(keys: List[int], freq: List[int]) -> int:
    """
    Optimized backtracking with early termination and better pruning.
    
    Args:
        keys: Sorted array of search keys
        freq: Frequency counts for each key
        
    Returns:
        Minimum cost of the optimal binary search tree
        
    Time Complexity: O(n³) with optimizations
    Space Complexity: O(n²)
    """
    if not keys or not freq or len(keys) != len(freq):
        return 0
    
    memo: Dict[Tuple[int, int], int] = {}
    
    def sum_freq(i: int, j: int) -> int:
        """Calculate sum of frequencies from index i to j."""
        return sum(freq[i:j+1])
    
    def opt_cost(i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return freq[i]
        
        state = (i, j)
        if state in memo:
            return memo[state]
        
        # Get sum of frequencies for this range
        fsum = sum_freq(i, j)
        
        # Try each key as root and find minimum cost
        min_cost = float('inf')
        
        # Optimization: Try middle elements first (often better)
        mid = (i + j) // 2
        for offset in range(j - i + 1):
            r = mid + offset if mid + offset <= j else i + (mid + offset - j - 1)
            if i <= r <= j:
                cost = opt_cost(i, r - 1) + opt_cost(r + 1, j)
                if cost < min_cost:
                    min_cost = cost
        
        memo[state] = min_cost + fsum
        return memo[state]
    
    return opt_cost(0, len(keys) - 1)


def analyze_obst_complexity(keys: List[int], freq: List[int]) -> Dict[str, any]:
    """
    Analyze the complexity and performance of different OBST implementations.
    
    Args:
        keys: Sorted array of search keys
        freq: Frequency counts for each key
        
    Returns:
        Dictionary with analysis results
    """
    results = {}
    
    # Test basic backtracking
    start_time = time.time()
    basic_result = obst_backtracking(keys, freq)
    basic_time = time.time() - start_time
    
    # Test memoized version
    start_time = time.time()
    memo_result = obst_backtracking_with_memoization(keys, freq)
    memo_time = time.time() - start_time
    
    # Test optimized version
    start_time = time.time()
    optimized_result = obst_backtracking_optimized(keys, freq)
    optimized_time = time.time() - start_time
    
    # Count structures
    start_time = time.time()
    cost, count = obst_backtracking_count_structures(keys, freq)
    count_time = time.time() - start_time
    
    results = {
        'keys_length': len(keys),
        'basic_backtracking': {
            'result': basic_result,
            'time': basic_time,
            'complexity': 'O(n * 2^n)'
        },
        'memoized': {
            'result': memo_result,
            'time': memo_time,
            'complexity': 'O(n³)'
        },
        'optimized': {
            'result': optimized_result,
            'time': optimized_time,
            'complexity': 'O(n³) with optimizations'
        },
        'structure_analysis': {
            'cost': cost,
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


def obst_backtracking_with_tree_building(keys: List[int], freq: List[int]) -> Tuple[int, Dict[int, Tuple[int, int]]]:
    """
    Find the optimal cost and build the tree structure.
    
    Args:
        keys: Sorted array of search keys
        freq: Frequency counts for each key
        
    Returns:
        Tuple of (minimum cost, tree structure where key -> (left_child, right_child))
        
    Time Complexity: O(n³) with memoization
    Space Complexity: O(n²)
    """
    if not keys or not freq or len(keys) != len(freq):
        return (0, {})
    
    memo: Dict[Tuple[int, int], int] = {}
    root_structure: Dict[Tuple[int, int], int] = {}
    
    def sum_freq(i: int, j: int) -> int:
        """Calculate sum of frequencies from index i to j."""
        return sum(freq[i:j+1])
    
    def opt_cost(i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return freq[i]
        
        state = (i, j)
        if state in memo:
            return memo[state]
        
        # Get sum of frequencies for this range
        fsum = sum_freq(i, j)
        
        # Try each key as root and find minimum cost
        min_cost = float('inf')
        best_root = i
        
        for r in range(i, j + 1):
            cost = opt_cost(i, r - 1) + opt_cost(r + 1, j)
            if cost < min_cost:
                min_cost = cost
                best_root = r
        
        memo[state] = min_cost + fsum
        root_structure[state] = best_root
        return memo[state]
    
    def build_tree_structure(i: int, j: int) -> Dict[int, Tuple[int, int]]:
        """Build the tree structure recursively."""
        if i > j:
            return {}
        
        if i == j:
            return {keys[i]: (-1, -1)}  # Leaf node
        
        root_idx = root_structure[(i, j)]
        root_key = keys[root_idx]
        
        # Build left subtree
        left_structure = build_tree_structure(i, root_idx - 1)
        
        # Build right subtree
        right_structure = build_tree_structure(root_idx + 1, j)
        
        # Combine structures
        tree_structure = left_structure.copy()
        tree_structure.update(right_structure)
        
        # Set root's children
        left_child = keys[root_idx - 1] if root_idx > i else -1
        right_child = keys[root_idx + 1] if root_idx < j else -1
        
        tree_structure[root_key] = (left_child, right_child)
        
        return tree_structure
    
    result = opt_cost(0, len(keys) - 1)
    tree_structure = build_tree_structure(0, len(keys) - 1)
    
    return (result, tree_structure)


def obst_backtracking_erickson_formulation(keys: List[int], freq: List[int]) -> int:
    """
    Direct implementation of Erickson's OptCost(i, k) formulation.
    
    This is the most direct translation of Erickson's recursive formulation:
    OptCost(i, k) = min(OptCost(i, r-1) + OptCost(r+1, k) + fsum) for r in [i, k]
    
    Args:
        keys: Sorted array of search keys
        freq: Frequency counts for each key
        
    Returns:
        Minimum cost of the optimal binary search tree
        
    Time Complexity: O(n * 2^n) - exponential
    Space Complexity: O(n) - recursion depth
    """
    if not keys or not freq or len(keys) != len(freq):
        return 0
    
    def sum_freq(i: int, j: int) -> int:
        """Calculate sum of frequencies from index i to j."""
        return sum(freq[i:j+1])
    
    def opt_cost(i: int, k: int) -> int:
        """
        Erickson's OptCost(i, k) formulation.
        
        Args:
            i: Start index of the range
            k: End index of the range
            
        Returns:
            Minimum cost of optimal BST for range [i, k]
        """
        if i > k:
            return 0  # No nodes in this range
        if i == k:
            return freq[i]  # Single node
        
        # Get sum of frequencies for this range
        fsum = sum_freq(i, k)
        
        # Try each key as root and find minimum cost
        min_cost = float('inf')
        for r in range(i, k + 1):
            # Cost = left subtree + right subtree + frequency sum
            cost = opt_cost(i, r - 1) + opt_cost(r + 1, k)
            if cost < min_cost:
                min_cost = cost
        
        return min_cost + fsum
    
    return opt_cost(0, len(keys) - 1)


def obst_backtracking_erickson_memoized(keys: List[int], freq: List[int]) -> int:
    """
    Erickson's formulation with memoization.
    
    Args:
        keys: Sorted array of search keys
        freq: Frequency counts for each key
        
    Returns:
        Minimum cost of the optimal binary search tree
        
    Time Complexity: O(n³) - memoization reduces exponential complexity
    Space Complexity: O(n²) - memo table
    """
    if not keys or not freq or len(keys) != len(freq):
        return 0
    
    memo: Dict[Tuple[int, int], int] = {}
    
    def sum_freq(i: int, j: int) -> int:
        """Calculate sum of frequencies from index i to j."""
        return sum(freq[i:j+1])
    
    def opt_cost(i: int, k: int) -> int:
        if i > k:
            return 0
        if i == k:
            return freq[i]
        
        state = (i, k)
        if state in memo:
            return memo[state]
        
        # Get sum of frequencies for this range
        fsum = sum_freq(i, k)
        
        # Try each key as root and find minimum cost
        min_cost = float('inf')
        for r in range(i, k + 1):
            cost = opt_cost(i, r - 1) + opt_cost(r + 1, k)
            if cost < min_cost:
                min_cost = cost
        
        memo[state] = min_cost + fsum
        return memo[state]
    
    return opt_cost(0, len(keys) - 1)


# Helper function for testing
def create_test_obst_cases() -> List[Tuple[List[int], List[int]]]:
    """Create various test cases for OBST testing."""
    return [
        ([], []),  # Empty case
        ([1], [10]),  # Single key
        ([1, 2], [34, 50]),  # Two keys
        ([10, 12, 20], [34, 8, 50]),  # Three keys
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Sequential
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),  # Reverse frequencies
        ([1, 2, 3, 4, 5], [10, 20, 30, 40, 50]),  # Increasing frequencies
        ([1, 2, 3, 4, 5], [50, 40, 30, 20, 10]),  # Decreasing frequencies
        ([1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 1, 1]),  # Equal frequencies
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 3, 2, 1]),  # Symmetric frequencies
    ] 