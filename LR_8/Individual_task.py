import random


class MersenneTwister:
    def __init__(self, seed):
        self.n = 7
        self.p = 2 ** self.n - 1
        self.x = [seed]  # Задание начального значения
        self.index = 0

        self.x[0] = seed

    def make_posled(self, posled_len):
        for i in range(1, posled_len):
            self.x.append((self.x[i - 1] * self.x[i - 1]) % self.p)

        for i in range(len(self.x)):
            self.x[i] <<= random.randint(0, self.n - 1)


def BPS(f, x, file_name):
    file = open(file_name, "a")
    alpha = []
    n = len(f)
    for i in range(n - 1):
        alpha.append(f[-(i + 1)])
    file.write("a: " + str(alpha) + "\n")
    n = len(alpha)
    for i in range(2 ** (len(f) - 1)):
        file.write(str(i) + ": " + str(x) + "\n")
        z = alpha[0] * x[-n]
        for j in range(1, n):
            z ^= alpha[j] * x[-n + j]
        x.append(z)
    file.close()


def It():
    f10 = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
    x10 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    BPS(f10, x10, "BPS_primitive_10.txt")
    f6 = [1, 0, 0, 0, 0, 1, 1]
    x6 = [1, 0, 0, 0, 0, 1]
    BPS(f6, x6, "BPS_primitive_6.txt")
    f14 = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1]
    x14 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    BPS(f14, x14, "BPS_primitive_14.txt")

    mt = MersenneTwister(5678)
    mt.make_posled(10)
    print(mt.x)
