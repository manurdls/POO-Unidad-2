from claseLista import Lista

from claseViajeroFrecuente import ViajeroFrecuente

class Menu(object):
    __switcher = None
    __viajeros = None
    __num_viajero = None

    def __init__(self, viajeros, num_viajero):
        self.__switcher = { 0:self.salir,
                            1:self.inciso1,
                            2:self.inciso2,
                            3:self.inciso3,
                         }
        self.__viajeros = viajeros
        self.__num_viajero = num_viajero

    def getSwitcher(self):
        return self.__switcher

    def option(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Fin programa')

    def inciso1(self):
        self.__viajeros.consultar_millas(self.__num_viajero)

    def inciso2(self):
        millas_recorridas = int(input("Ingrese las millas recorridas: "))
        self.__viajeros.acumular_millas(self.__num_viajero, millas_recorridas)

    def inciso3(self):
        millas_a_canjear = int(input("Ingrese las millas a canjear: "))
        self.__viajeros.canjear_millas(self.__num_viajero, millas_a_canjear)
    