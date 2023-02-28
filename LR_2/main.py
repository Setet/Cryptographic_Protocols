# расширенный евклид
def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_euclidean(b % a, a)
        return g, x - (b // a) * y, y


# модульная обратная функция
def modinv(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m


# функция кит теоремы
def crt(m, x):
    while True:

        temp1 = modinv(m[1], m[0]) * x[0] * m[1] + \
                modinv(m[0], m[1]) * x[1] * m[0]

        temp2 = m[0] * m[1]
        print("Temp 1: " + str(temp1))
        print("Temp 2: " + str(temp1))

        # это я удаляю первые два элемента
        # из списка остатков и заменяю
        # с остатком, который будет
        # быть temp1 % temp2
        x.remove(x[0])
        x.remove(x[0])
        x = [temp1 % temp2] + x

        # затем я удаляю первые два значения из
        # списка модулей, так как они мне больше не нужны
        # и их просто заменил новыми
        # модулями, которые я рассчитал
        m.remove(m[0])
        m.remove(m[0])
        m = [temp2] + m

        if len(x) == 1:
            break

    return x[0]


def main():
    # список m содержит все модули
    # list x содержит остатки уравнений
    # Пример my=x(mod m)
    x = [1, 1, 0]
    m = [3, 4, 7]
    print(crt(m, x))


if __name__ == '__main__':
    main()
