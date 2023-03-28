# возвращает i-й бит числа x
def bit(x, i):
    return (x >> i) & 1


# генератор Блюм-Блюм-Шуба с заданными параметрами
def blum_blum_shub(seed, p, q, n):
    x = seed
    while True:
        x = (x ** 2) % n
        yield bit(x, 0)


def blum_blum():
    p = 986731103
    q = 982449941
    n = p * q
    seed = 1234567890

    gen = blum_blum_shub(seed, p, q, n)

    # выводим первые 10 бит генератора
    for i in range(10):
        print(next(gen))
