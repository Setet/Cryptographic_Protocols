import math


def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

    # Чтобы проверить все числа вида 6k ± 1
    # пока i <= квадратный корень из n, с шагом 6
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


if __name__ == '__main__':
    test1 = 11
    test2 = 20
    test3 = 41
    print(f"Число:{test1} - Простота:{isPrime(test1)}")
    print(f"Число:{test2} - Простота:{isPrime(test2)}")
    print(f"Число:{test3} - Простота:{isPrime(test3)}")
