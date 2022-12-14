# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Journal:
    def __init__(self, colour: str, pages: int):
        if not isinstance(colour, str):
            raise TypeError #not type str

        self.colour = colour

        if not isinstance(pages, int):
            raise TypeError #not type int
        if pages <= 0:
            raise ValueError #no pages

        self.pages = pages

    def read_journal(self) -> None:
        ...

class University:
    def __init__(self, floors: int, classes: int):
        if not isinstance(floors, int):
            raise TypeError #not type int
        if floors <= 0:
            raise ValueError #uni should have at least 1 floor

        self.floors = floors

        if not isinstance(classes, int):
            raise TypeError #not type int
        if classes <= 4:
            raise ValueError #uni should have at least 5 classes

        self.classes = classes

class Traffic_light: #Светофор

    def __init__(self, lights: int, legs: int, location: str):
        if not isinstance(lights, int):
            raise TypeError
        if lights != 3:
            raise ValueError #should have 3 lights

        self.lights = lights

        if not isinstance(legs, int):
            raise TypeError
        if legs != 1:
            raise ValueError #should have 1 leg

        self.legs = legs

        if not isinstance(location, str):
            raise TypeError

        self.location = location

if __name__ == "__main__":

    Journal123 = Journal("Красный", 33)
    Journal321 = Journal("Белый", 10)

    Polytech1 = University(1000, 1000)
    Polytech2 = University(100, 100)

    Light1 = Traffic_light(3, 1, "Москва")
    Light2 = Traffic_light(3, 1, "Орел")

    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
