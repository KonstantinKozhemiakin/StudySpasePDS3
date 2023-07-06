import string
import sys


class Car:
    def __init__(self, brand, color, engine_capacity):
        self.__brand = brand
        self.__color = color
        self.__engine_capacity = engine_capacity

    def move_forward(self):
        print("The car is moving forward")

    def move_backward(self):
        print("The car is moving backward")


class CarUpd(Car):
    def move_left(self):
        print("The car is going to the left")

    def move_right(self):
        print("The car is going to the right")


class TextProcessor:
    def __init__(self):
        self._punktuation = string.punctuation

    def get_clean_text(self, text):
        clean_text = ""
        for i in range(len(text)):
            if not self.__is_punctiantian(text[i]):
                clean_text += text[i]
        return clean_text

    def __is_punctiantian(self, symb):
        return symb in self._punktuation


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ""

    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_text(text)

    def get_clean_text(self):
        return self.__clean_string

    @property
    def attention(self):
        print("Attention, the cleaned text is displayed", file=sys.stderr)


class DataInterface:
    def __init__(self):
        self._text_loader = TextLoader()

    def process_text(self, list_text):
        self._text_loader.attention
        for i in range(len(list_text)):
            self._text_loader.set_clean_text(list_text[i])
            print(self._text_loader.get_clean_text())


class Parallelogram:
    def __init__(self, width=0, length=0):
        self._width = width
        self._length = length

    def get_area(self):
        return self._width * self._length


class Square(Parallelogram):
    def get_area(self):
        return self._width ** 2

# car = Car("Volvo", "Orange", 2.0)
# car.move_forward()
# car.move_backward()
#
# car_upd = CarUpd("Volvo", "Orange", 2.0)
# car_upd.move_forward()
# car_upd.move_backward()
# car_upd.move_right()
# car_upd.move_left()
#
# proc = TextProcessor()
# print(proc.get_clean_text("hghgh./ghger''4326bgfdn"))
# text_loader = TextLoader()
# text_loader.set_clean_text("s?sss,ss/s*sss")
# my_list = ["11,1.1/1", "222;'222", "3abcd", ",.;/"]
# data_interface = DataInterface()
# data_interface.process_text(my_list)
# par = Parallelogram(10, 5)
# print(par.get_area())
# square = Square(9)
# print(square.get_area())
