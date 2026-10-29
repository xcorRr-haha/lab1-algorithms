import sys
import os
import random

# Добавляем папку src в пути, чтобы Python видел algorithms.py и generator.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from algorithms import two_pointers, binary_search, exponential, double_binary
from generator import generate_sample

ALGORITHMS = [two_pointers, binary_search, exponential, double_binary]

def run_tests():
    print("Запуск тестов на корректность...\n")
    
    # 1. Проверяем на жестко заданных примерах из задания
    fixed_cases = [
        ([1, 2, 3], [3, 4, 5], True),
        ([2, 4, 6], [3, 5, 7], False),
        ([], [], False),
        ([], [1, 2, 3], False),
        ([1], [1], True),
        ([-10, -5, 0], [-3, -2, 0], True),
    ]
    
    print("--- Проверка на примерах из задания ---")
    for func in ALGORITHMS:
        for i, (a, b, expected) in enumerate(fixed_cases):
            res = func(a[:], b[:])
            if res != expected:
                print(f"ОШИБКА в {func.__name__} на тесте {a}, {b}. Ожидали {expected}, получили {res}")
                return
    print("Все алгоритмы прошли базовые тесты!\n")

    # 2. Проверяем на сгенерированных случайных данных
    print("--- Проверка на сгенерированных данных (рандом) ---")
    # Прогоняем 100 случайных тестов разных размеров
    for _ in range(100):
        m = random.randint(1, 50)
        n = random.randint(1, 50)
        
        # С вероятностью 50% делаем так, чтобы общий элемент был
        has_common = random.random() > 0.5
        
        a, b, expected = generate_sample(m, n, has_common)
        
        for func in ALGORITHMS:
            res = func(a[:], b[:])
            if res != expected:
                print(f"ОШИБКА в {func.__name__} на сгенерированных массивах:")
                print(f"A = {a}")
                print(f"B = {b}")
                print(f"Ожидали {expected}, получили {res}")
                return
    
    print("Все алгоритмы прошли тесты на сгенерированных данных!\n")
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! Алгоритмы работают верно.")

if __name__ == "__main__":
    run_tests()