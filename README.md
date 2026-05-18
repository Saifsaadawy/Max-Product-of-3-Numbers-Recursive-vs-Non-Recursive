<div align="center">

# 📊 Max Product of Three — Algorithm Analysis

**A Python project that implements and compares two algorithms for finding the maximum product of any triplet in an array — Iterative (O(n²)) vs Recursive (O(n³)).**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![Topic](https://img.shields.io/badge/Topic-Algorithm%20Analysis-orange?style=flat-square)](/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Problem Statement](#-problem-statement)
- [Algorithms](#-algorithms)
- [Complexity Comparison](#-complexity-comparison)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How to Run](#-how-to-run)
- [Sample Output](#-sample-output)

---

## 🧾 About

This project was built for an Algorithm Analysis course. It explores two different approaches to solving the **Maximum Product of Three** problem — one iterative using sorting, and one recursive using combination enumeration — then compares their correctness, time complexity, space complexity, and real execution time.

---

## 🧩 Problem Statement

Given an array `A` of `N` integers, find the **maximum product** of any three elements `A[P] × A[Q] × A[R]` where `0 ≤ P < Q < R < N`.

```
Input:  [-3, 1, 2, -2, 5, -6]
Output: 90   → (-3) × (-6) × 5 = 90
```

> The trick: two large negatives multiplied together give a large positive — so sorting alone and picking the top three isn't always correct.

---

## 🧠 Algorithms

### Algorithm 1 — Iterative (Sort-based)

```
Algorithm maxProduct(A, N):
    insertion_sort(A)                      ← sort descending
    max_product1 ← A[0] × A[1] × A[2]    ← three largest
    max_product2 ← A[0] × A[n-2] × A[n-1] ← one large + two most negative
    return max(max_product1, max_product2)
```

Uses **insertion sort** (descending) then compares two candidates:
- Three largest positives
- The largest positive × the two most negative (product of two negatives = positive)

---

### Algorithm 2 — Recursive (Combination Enumeration)

```
Algorithm helper(A, n, count, start, current_product):
    if count == 3:
        return current_product          ← base case: triplet complete

    best ← -∞
    for i from start to (n - (2 - count)):
        result ← helper(A, n, count+1, i+1, current_product × A[i])
        best ← max(best, result)
    return best
```

Recursively enumerates **every possible triplet** and returns the maximum product found. Correct but slower — explores all C(n, 3) combinations.

---

## 📐 Complexity Comparison

| Feature | Algorithm 1 — Iterative | Algorithm 2 — Recursive |
|---|---|---|
| Approach | Insertion sort + two candidates | Recursive triplet enumeration |
| Time Complexity | **O(n²)** | **O(n³)** |
| Space Complexity | **O(1)** | **O(n)** (call stack) |
| Handles negatives | ✅ Yes | ✅ Yes |
| Stack overflow risk | ❌ None | ⚠️ Yes (large n) |
| Readability | Clear | Moderate |
| Best for | General / production use | Learning recursion |

**Conclusion:** The iterative approach is preferable in practice — same correctness, better time and space complexity.

---

## 📁 Project Structure

```
max_product_project/
│
├── algorithm1_iterative.py   # Iterative solution (insertion sort + two candidates)
├── algorithm2_recursive.py   # Recursive solution (triplet enumeration)
├── comparison.py             # Correctness check + performance benchmark + summary
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8** or higher (no external libraries needed)

### Install

```bash
git clone https://github.com/YOUR_USERNAME/max-product-project.git
cd max-product-project
```

---

## ▶️ How to Run

### Run Algorithm 1 (Iterative) standalone

```bash
python algorithm1_iterative.py
```

Runs 3 built-in test cases then prompts for custom input:
```
Enter array of numbers (space separated): -3 1 2 -2 5 -6
Result: 90
```

### Run Algorithm 2 (Recursive) standalone

```bash
python algorithm2_recursive.py
```

Same format — built-in tests then custom input prompt.

### Run full comparison

```bash
python comparison.py
```

Outputs:
1. **Correctness check** — both algorithms tested against 4 edge cases
2. **Performance benchmark** — execution time for n = 10, 20, 50, 100
3. **Summary table** — side-by-side comparison of all metrics

---

## 🖥️ Sample Output

```
====================================================
  CORRECTNESS CHECK
====================================================

  [✓ PASS] All positives (small)
    Input    : [1, 2, 3]
    Expected : 6
    Iter     : 6
    Recur    : 6

  [✓ PASS] Two large negatives
    Input    : [-10, -10, 1, 3, 2]
    Expected : 300
    Iter     : 300
    Recur    : 300

====================================================
  PERFORMANCE COMPARISON  (time in ms)
====================================================
       n     Iterative     Recursive
  --------------------------------------
      10        0.0021        0.0085
      20        0.0038        0.0612
      50        0.0201        0.9134
     100        0.0743       12.4210

====================================================
  ALGORITHM SUMMARY
====================================================
  Feature                Iterative       Recursive
  Time Complexity        O(n^2)          O(n^3)
  Space Complexity       O(1)            O(n)
  Best for               General use     Learning recursion
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
  Built with Python 🐍 &nbsp;·&nbsp; Algorithm Analysis Course Project
</div>
