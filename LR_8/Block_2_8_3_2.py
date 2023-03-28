import numpy as np


# Рекуррентная формула для вычисления следующего элемента
def next_element(seq, delays, gf2_3):
    next_elem = gf2_3[0]
    for delay in delays:
        next_elem ^= seq[-delay]
    return next_elem


def fibon_2():
    # Определение поля Галуа GF(2^3)
    gf2_3 = np.array([0, 1, 2, 4])

    # Выбор начальных элементов a0 и a1
    a0 = gf2_3[1]
    a1 = gf2_3[2]

    # Определение количества запаздываний
    num_delays = 2

    # Определение запаздываний для каждого элемента
    delays = [(1, 2), (2, 3)]

    # Вычисление последовательности
    seq = [a0, a1]
    for i in range(num_delays, 10):
        seq.append(next_element(seq, delays[i - num_delays:i], gf2_3))

    # Печать результата
    print(seq)
