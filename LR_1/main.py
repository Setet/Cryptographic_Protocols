from datetime import datetime
import random


def phi_formula(n):
    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1

    if n > 1:
        result -= result // n

    return int(result)


# Функция для НОД-а
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def phi_definition(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


def main():
    items = [random.randint(10000000, 20000000) for i in range(100)]
    counter = 0
    print("По определению :")
    all_start_time = datetime.now()
    for n in items:
        counter += 1
        print(str(counter) + ")" + "phi(", n, ") = ",
              phi_definition(n), sep="")
    all_over_time = datetime.now() - all_start_time
    print("Суммарное время на массив :" + str(all_over_time))

    print("По формуле :")
    all_start_time = datetime.now()
    for n in items:
        counter += 1
        print(str(1) + ")" + "phi(", n, ") = ",
              phi_formula(n), sep="")
    all_over_time = datetime.now() - all_start_time
    print("Суммарное время на массив :" + str(all_over_time))


if __name__ == '__main__':
    main()