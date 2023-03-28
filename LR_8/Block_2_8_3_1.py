class FibonacciGenerator:
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


def fibon_1(n):
    fib = FibonacciGenerator()
    for i in range(n):
        print(next(fib))
