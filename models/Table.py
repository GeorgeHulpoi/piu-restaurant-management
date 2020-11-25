from enum import Enum

class Table:
    def __init__(self, id, x, y, rotation, type):
        self.__id = id
        self.__x = x
        self.__y = y
        self.__rotation = rotation
        self.__type = type

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def getRotation(self):
        return self.__rotation

    def setRotation(self, rotation):
        self.__rotation = rotation

    def getType(self):
        return self.__type

    def setType(self, type):
        self.__type = type

class TableType(Enum):
    ROUND_4 = 0
    RECTANGLE_4 = 1
    RECTANGLE_6 = 2
