class Vertice(object):
    __x = None
    __y = None

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        s = '({},{})'.format(self.__x, self.__y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y