"""
===================================================
Max Product of Three - Algorithm 2 (Recursive)
===================================================

Pseudo Code:
------------
Algorithm helper(A, n, count, start, current_product):
    if count == 3:
        return current_product          // base case: triplet complete

    best = -infinity
    for i from start to (n - (2 - count)):
        result = helper(A, n, count+1, i+1, current_product * A[i])
        if result > best:
            best = result
    return best

Algorithm maxProduct(A):
    return helper(A, len(A), 0, 0, 1)

Time  Complexity: O(n^3)  -- same combinations explored as iterative
Space Complexity: O(n)    -- recursive call stack depth up to 3 levels
                            (but grows with n due to the loop depth)
"""


def _helper(A, n, count, start, current_product):
    """
    Recursive helper that builds every triplet combination.

    Parameters:
        A               : the array
        n               : length of A
        count           : how many elements chosen so far (0, 1, or 2)
        start           : next index to consider
        current_product : product of elements chosen so far

    Returns:
        int: best (maximum) product reachable from this state
    """
    # Base case: we have picked exactly 3 elements
    if count == 3:
        return current_product

    best = float('-inf')

    # Try every valid next index
    for i in range(start, n - (2 - count)):
        result = _helper(
            A, n,
            count + 1,        # one more element chosen
            i + 1,            # next element must be strictly after i
            current_product * A[i]
        )
        if result > best:
            best = result

    return best


def maxProduct_recursive(A):
    """
    Returns the maximum product of any triplet (P, Q, R)
    where 0 <= P < Q < R < N.

    Parameters:
        A (list): Non-empty zero-indexed array of integers

    Returns:
        int: The maximum product of any triplet
    """
    return _helper(A, len(A), 0, 0, 1)


# ─────────────────────────── Tests ───────────────────────────
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3],          6),
        ([1, 2, 3, 4],       24),
        ([-3, 1, 2, -2, 5, 6], 60),
    ]

    print("=== Algorithm 2: Recursive ===\n")
    for nums, expected in test_cases:
        result = maxProduct_recursive(nums)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"  Input:    {nums}")
        print(f"  Expected: {expected}  |  Got: {result}  {status}\n")
    try:
        arr_string = input("Enter array of numbers (space separated): ").strip()
        if arr_string:
            arr = [int(i) for i in arr_string.split()]
            if len(arr) > 2:
                print(f"Result: {maxProduct_recursive(arr)}")
            else:
                print("=========================================\nPlease enter at least three numbers.")
        else:
            print("=========================================\nPlease enter valid numbers only.")
    except ValueError:
        print("=========================================\nPlease enter valid numbers only.")