"""
===================================================
Comparison & Analysis: Algorithm 1 vs Algorithm 2
===================================================
"""

import time
import random
from algorithm1_iterative import maxProduct_iterative
from algorithm2_recursive import maxProduct_recursive


def measure_time(func, A, runs=5):
    """Run func(A) multiple times and return average time in ms."""
    total = 0
    for _ in range(runs):
        start = time.perf_counter()
        func(A)
        total += time.perf_counter() - start
    return (total / runs) * 1000   # convert to milliseconds


# ─────────────── Correctness Check ───────────────
def correctness_check():
    print("=" * 52)
    print("  CORRECTNESS CHECK")
    print("=" * 52)

    test_cases = [
        ([1, 2, 3],             6,  "All positives (small)"),
        ([1, 2, 3, 4],          24, "All positives (4 elements)"),
        ([-3, 1, 2, -2, 5, 6],  60, "Mixed negatives & positives"),
        ([-10, -10, 1, 3, 2],   300,"Two large negatives"),
    ]

    all_pass = True
    for nums, expected, desc in test_cases:
        r1 = maxProduct_iterative(nums)
        r2 = maxProduct_recursive(nums)
        ok = (r1 == expected and r2 == expected)
        status = "✓ PASS" if ok else "✗ FAIL"
        if not ok:
            all_pass = False
        print(f"\n  [{status}] {desc}")
        print(f"    Input    : {nums}")
        print(f"    Expected : {expected}")
        print(f"    Iter     : {r1}")
        print(f"    Recur    : {r2}")

    print("\n" + ("All tests passed!" if all_pass else "Some tests FAILED!"))
    print()


# ─────────────── Performance Comparison ───────────────
def performance_comparison():
    print("=" * 52)
    print("  PERFORMANCE COMPARISON  (time in ms)")
    print("=" * 52)
    print(f"  {'n':>6}  {'Iterative':>12}  {'Recursive':>12}")
    print("  " + "-" * 38)

    for n in [10, 20, 50, 100]:
        A = [random.randint(-100, 100) for _ in range(n)]
        t_iter = measure_time(maxProduct_iterative, A)
        t_rec  = measure_time(maxProduct_recursive, A)
        print(f"  {n:>6}  {t_iter:>11.4f}  {t_rec:>11.4f}")

    print()


# ─────────────── Summary Table ───────────────
def print_summary():
    print("=" * 52)
    print("  ALGORITHM SUMMARY")
    print("=" * 52)
    rows = [
        ("Feature",           "Iterative",    "Recursive"),
        ("-" * 20,            "-" * 12,       "-" * 12),
        ("Approach",          "Sorting",      "Recursion"),
        ("Time Complexity",   "O(n^2)",        "O(n^3)"),
        ("Space Complexity",  "O(1)",          "O(n)"),
        ("Readability",       "Clear",         "Moderate"),
        ("Stack Overflow Risk","None",         "Yes (large n)"),
        ("Best for",          "General use",  "Learning recursion"),
    ]
    for r in rows:
        print(f"  {r[0]:<22} {r[1]:<14} {r[2]}")
    print()
    print("  Conclusion:")
    print("    Iterative algorithms [O(n^2)] is greater than Recursive algorithms [O(n^3)]")
    print("    The iterative version is preferable in practice")
    print("    because it uses O(1) space vs O(n) for the call stack.")
    print()


if __name__ == "__main__":
    correctness_check()
    performance_comparison()
    print_summary()
