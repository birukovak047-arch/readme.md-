def square(size):
    if size % 1 == 0:
        return size * size
    else:
        import math
        return math.ceil(size) * math.ceil(size)

a = float(input("Введите сторону квадрата: "))
print(square(a))