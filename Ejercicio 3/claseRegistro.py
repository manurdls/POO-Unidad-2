

class Registro(object):

    __temperatura: int
    __humedad: int
    __presion: int

    def __init__(self, temp, hum, pres):
        self.__temperatura = temp
        self.__humedad = hum
        self.__presion = pres

    def __str__(self):
        s = 'Temperatura: {}, Humedad: {}, Presion: {}'.format(self.__temperatura, self.__humedad, self.__presion)
        return s

    def get_temperatura(self):
        return self.__temperatura

    def get_humedad(self):
        return self.__humedad

    def get_presion(self):
        return self.__presion

    