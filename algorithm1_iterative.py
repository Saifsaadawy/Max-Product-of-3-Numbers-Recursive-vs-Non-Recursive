"""
===================================================
Max Product of Three - Algorithm 1 (Non-Recursive)
===================================================

Pseudo Code:
------------
Algorithm maxProduct(A, N):
    insertion_sort(A)
    max_product1 <- A[0] * A[1] * A[2]
    max_product2 <- A[0] * A[n-2] * A[n-1]
    if max_product1 > max_product2
        return max_product1
    else
        return max_product2

Algorithm insertion_sort(A):
    for i <- 1 to n do
       key <- A[i]
       j <- i-1
       while j >= 0 and key > A[j]:
            A[j+1] <- A[j]
            j <- j - 1
       A[j+1] <- key

Time  Complexity: O(n^2)  -- sorting then choosing the biggest value
Space Complexity: O(1)    -- only a few variables used
"""


def maxProduct_iterative(A):

    n = len(A)
    insertion_sort(A)
    max_product1 = A[0] * A[1] * A[2]
    max_product2 = A[0] * A[n-2] * A[n-1]
    if max_product1 > max_product2 :
        return max_product1
    else:
        return max_product2

def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j >= 0 and key > A[j]:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key

# ─────────────────────────── Tests ───────────────────────────
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3],          6),
        ([1, 2, 3, 4],       24),
        ([-3, 1, 2, -2, 5, -6], 90),
    ]
    print("=== Algorithm 1: Iterative (Non-Recursive) ===\n")
    for nums, expected in test_cases:
        result = maxProduct_iterative(nums)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"  Input:    {nums}")
        print(f"  Expected: {expected}  |  Got: {result}  {status}\n")
    try:
        arr_string = input("Enter array of numbers (space separated): ").strip()
        if arr_string:
            arr = [int(i) for i in arr_string.split()]
            if len(arr) > 2:
                print(f"Result: {maxProduct_iterative(arr)}")
            else:
                print("=========================================\nPlease enter at least three numbers.")
        else:
            print("=========================================\nPlease enter valid numbers only.")
    except ValueError:
            print("=========================================\nPlease enter valid numbers only.")
