import sys
import os
import time
import csv

sys.path.insert(0, os.path.dirname(__file__))

from algorithms import two_pointers, binary_search, exponential, double_binary
from generator import generate_sample

ALGORITHMS = {
    "two_pointers": two_pointers,
    "binary_search": binary_search,
    "exponential": exponential,
    "double_binary": double_binary,
}

def run_benchmark():
    os.makedirs("data", exist_ok=True)
    results = []
    
    print("Начинаем замеры времени...")
    
    def get_average_time(func, a, b):
        func(a, b)
        total_time = 0
        for _ in range(100):
            start = time.perf_counter()
            func(a, b)
            total_time += (time.perf_counter() - start)
        return total_time / 100

    print("\nСценарий 1: M = N")
    sizes_equal = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
    for size in sizes_equal:
        a, b, _ = generate_sample(size, size, want_intersection=False)
        for name, func in ALGORITHMS.items():
            avg_time = get_average_time(func, a, b)
            results.append({"scenario": "M=N", "M": size, "N": size, "ratio": 1, "algorithm": name, "time_sec": avg_time})
            print(f"  {name:15} | M={size:<7} N={size:<7} | {avg_time:.6f} сек")

    print("\nСценарий 2: M = 100, N растет")
    M_FIXED = 100
    sizes_n = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
    for size_n in sizes_n:
        a, b, _ = generate_sample(M_FIXED, size_n, want_intersection=False)
        for name, func in ALGORITHMS.items():
            repeats = 100 if size_n <= 50000 else 10
            func(a, b)
            total_time = 0
            for _ in range(repeats):
                start = time.perf_counter()
                func(a, b)
                total_time += (time.perf_counter() - start)
            avg_time = total_time / repeats
            
            results.append({"scenario": "M=100", "M": M_FIXED, "N": size_n, "ratio": size_n/M_FIXED, "algorithm": name, "time_sec": avg_time})
            print(f"  {name:15} | M={M_FIXED:<7} N={size_n:<9} | {avg_time:.6f} сек")

    print("\nСценарий 3: N = 100 000, N/M растет")
    N_FIXED = 100000
    ratios = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    for r in ratios:
        size_m = max(1, int(N_FIXED / r))
        a, b, _ = generate_sample(size_m, N_FIXED, want_intersection=False)
        for name, func in ALGORITHMS.items():
            func(a, b)
            total_time = 0
            for _ in range(100):
                start = time.perf_counter()
                func(a, b)
                total_time += (time.perf_counter() - start)
            avg_time = total_time / 100
            
            results.append({"scenario": "Varying ratio", "M": size_m, "N": N_FIXED, "ratio": r, "algorithm": name, "time_sec": avg_time})
            print(f"  {name:15} | M={size_m:<7} N={N_FIXED:<7} (N/M={r:<5.1f}) | {avg_time:.6f} сек")

    csv_path = os.path.join("data", "results.csv")
    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["scenario", "M", "N", "ratio", "algorithm", "time_sec"])
        writer.writeheader()
        writer.writerows(results)
        
    print(f"\nГотово! Данные в {csv_path}")

if __name__ == "__main__":
    run_benchmark()