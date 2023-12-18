import timeit
from functools import lru_cache

# Итеративная версия для вычисления факториала
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Рекурсивная версия для вычисления факториала
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Итеративная версия для вычисления чисел Фибоначчи
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Рекурсивная версия для вычисления чисел Фибоначчи
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Используем timeit для измерения времени выполнения функций
print("Итеративный факториал:", timeit.timeit(lambda: factorial_iterative(10), number=100000))
print("Рекурсивный факториал:", timeit.timeit(lambda: factorial_recursive(10), number=100))

print("Итеративное число Фибоначчи:", timeit.timeit(lambda: fib_iterative(10), number=100000))
print("Рекурсивное число Фибоначчи:", timeit.timeit(lambda: fib_recursive(10), number=100))

# Применяем lru_cache к рекурсивным функциям
factorial_recursive = lru_cache()(factorial_recursive)
fib_recursive = lru_cache()(fib_recursive)

# Измеряем время выполнения после применения lru_cache
print("Рекурсивный факториал (с lru_cache):", timeit.timeit(lambda: factorial_recursive(10), number=100))
print("Рекурсивное число Фибоначчи (с lru_cache):", timeit.timeit(lambda: fib_recursive(10), number=100))
