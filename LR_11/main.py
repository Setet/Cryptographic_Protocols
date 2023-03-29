import math


def left_rotate(value, shift):
    return ((value << shift) & 0xffffffff) | (value >> (32 - shift))


def md5(message):
    message = bytearray(message, 'utf-8')

    # Исходные значения, определенные в стандарте MD5
    initial_values = [int('0x67452301', 16),
                      int('0xEFCDAB89', 16),
                      int('0x98BADCFE', 16),
                      int('0x10325476', 16)]

    # Смещения для каждого из 64 раундов
    shift_amounts = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                     5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
                     4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                     6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

    # Константы для каждого из 64 раундов
    constants = [int(math.floor(abs(math.sin(i + 1)) * (2 ** 32))) for i in range(64)]

    # Добавление бита '1' в конец сообщения
    message.append(128)  # 0b10000000

    # Добавление нулевых битов до длины сообщения в 64 байта
    while len(message) % 64 != 56:
        message.append(0)

    # Добавление длины сообщения в конец в битах (little-endian)
    message_length = len(message) * 8
    message += message_length.to_bytes(8, byteorder='little')

    # Итерация по блокам сообщения
    for i in range(0, len(message), 64):
        block = message[i:i + 64]

        # Инициализация хеша текущего блока значениями из предыдущего хеша
        a, b, c, d = initial_values

        # Основной цикл-шаг алгоритма MD5
        for j in range(64):

            # Вычисление функции F, G, H или I в зависимости от номера шага
            if 0 < j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif 16 < j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif 32 < j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * j) % 16

            # Вычисление новых значений переменных на текущем шаге
            temp = d
            d = c
            c = b
            b = b + left_rotate((a + f + constants[j] + int.from_bytes(block[g * 4:g * 4 + 4],
                                                                       byteorder='little')), shift_amounts[j])
            a = temp

        # Обновление значений хеша значениями соответствующих переменных на текущем блоке
        initial_values[0] += a
        initial_values[1] += b
        initial_values[2] += c
        initial_values[3] += d

    # Объединение значений хеша в один 128-битный хеш
    hash_value = sum(x << (32 * i) for i, x in enumerate(initial_values))
    return '{:032x}'.format(hash_value)


'''
В этой реализации используется bytearray для преобразования входного сообщения в байтовую строку в кодировке UTF-8,
 как рекомендовано в стандарте MD5.
Функция left_rotate выполняет циклический сдвиг битов числа на заданное количество позиций влево,
 сохраняя его 32-битную длину.
Функция md5 реализует основную логику алгоритма MD5, включая итерацию по блокам сообщения,
 основной цикл-шаг и объединение значений хеша.
Для вычисления каждого значения переменной используются соответствующие операции и вычисления, описанные в стандарте.
Форматирование результата в строку с 32-значным шестнадцатеричным числом 
('{:032x}'.format(hash_value)) обеспечивает правильный формат вывода хеша.
'''
if __name__ == '__main__':
    message = 'Wake the fuck up, samurai! We have a city to burn.'
    print(md5(message))
