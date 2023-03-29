from Block_2_8_3_1 import fibon_1
from Block_2_8_3_2 import fibon_2
from Block_8_4 import blum_blum
from Individual_task import It


def main():
    fibon_n = 10
    print(f"Генератор последовательности Фиббоначи с запаздываниями для {fibon_n} целых чисел")
    fibon_1(fibon_n)
    # print(f"Генератор последовательности Фиббоначи с запаздываниями для элементов произвольного поля Галуа GF(2^n)")
    # fibon_2()
    print(f"Генератор Блюм-Блюм-Шуба для произвольных параметров")
    blum_blum()
    print(f"Куча всяких приколов")
    It()


if __name__ == '__main__':
    main()
