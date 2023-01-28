# # PascalCase
# from pathlib import Path
#
#
# class FileManager:
#     BASE_DIR = Path(__file__).resolve().parent
#     file_path = BASE_DIR / "test.py"
#
#     def read(self, encoding: str = 'utf-8'):
#         with open(self.file_path, 'r', encoding=encoding) as f:
#             result = f.read()
#         return result
#
#     def write(self, content: str, encoding: str = 'utf-8'):
#         with open(self.file_path, 'w', encoding=encoding) as f:
#             result = f.write(content)
#         return result
#
#
# list_1 = [1, 2, 3]
# list_1.pop()


# class Bike:
#     wheels = 2
#     pedals = 1
#     seat = 1


# Bike.wheels = 5
# bike_1.wheels = 4
# print(bike_1.wheels)
# Bike.wheels = 3
# bike_2 = Bike()
# print(Bike.wheels)
# print(bike_2.wheels)
# bike_3 = Bike()
# print(bike_3.wheels)
# print(bike_1.steel)
# bike_1 = Bike()
# Bike.wheels = 3
# bike_1.wheels = 4
# print(Bike.wheels)
# print(bike_1.wheels)
# bike_1.steel = "alumin"
# print(bike_1.steel)
# print(bike_1.pedals)
# print(bike_1.seat)
# print(dir(Bike))
# print(dir(bike_1))
# print(type([1, 2, 3]))
# print(type(bike_1))
# print(type(Bike))
# print(type(list))


class Square:
    a = 20

    def __init__(self, adfdsdsa: int = None, dsadasd: int = 0):
        if adfdsdsa:
            self.x = adfdsdsa
        self.a = dsadasd

    def perimeter(self):
        return self.x * 4

    def area(self):
        return self.x ** 2

    def __add__(self, other):
        self.a += other
        return self.a

    def __mul__(self, other):
        self.a *= other
        return self.a

    def __sub__(self, other):
        pass


# square = Square(a=30)  # X132432432
# print(square.x)
# square1 = Square(20, 40)  # X132432432
# print(square1.x)
# square2 = Square(30, 50)  # X132432432
# print(square2.x)
# square3 = Square(40, 60)  # X132432432
# print(square3.x)
# square_2 = Square(20, 30)  # X232432432
# square_2.x = 30
# square.x = 20
# print(square)
# print(square.perimeter())
# print(square.area())
# print(isinstance(square, list))

# square = Square(20, 30)
# square.per = 500
# square2 = Square(20, 30)
# print(hasattr(square, "per"))
# print(hasattr(square2, "per"))
# if hasattr(square2, 'per'):
#     print(square2.per)
# if hasattr(square, 'per'):
#     print(square.per)
# setattr(square, 'per2', 500)
# print(square.per2)
# if hasattr(square, 'per'):
#     delattr(square, 'per')
# print(square.per)
# print(getattr(square, 'per3', None))
# if hasattr(square, 'per'):
#     setattr(square, 'per', 200)
#     # square.per = 200
#     print(square.per)
# print(square2.per)

# s = Square(20, 30)
# print(s + 30)
# print(s * 30)
# print(30 + s.a)
# print(s + Square(20, 340))
