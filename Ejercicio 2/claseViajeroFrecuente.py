

class ViajeroFrecuente(object):

    __num_viajero = None
    __dni = None
    __nombre = None
    __apellido = None
    __millas_acum = None

    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
    
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def __str__(self):
        return "{} {}".format(self.__nombre, self.__apellido)

    def getNumViajero(self):
        return self.__num_viajero
    
    def cantidadTotalMillas(self) -> int:
        return self.__millas_acum

    def acumularMillas(self, millas) -> int:
        if (type(millas) == int and millas > 0):
            self.__millas_acum += millas
        return self.__millas_acum


    def canjearMillas(self, millas) -> int:
        if (type(millas) == int and millas > 0):
            if (millas <= self.__millas_acum):
                self.__millas_acum -= millas
            else:
                print("Error: millas acumuladas insuficientes")
        return self.__millas_acum