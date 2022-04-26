from claseLista import Lista

from claseViajeroFrecuente import ViajeroFrecuente

class Menu(object):
    __switcher = None
    __viajeros = None

    def __init__(self, viajeros):
        self.__switcher = { 0:self.salir,
                            1:self.inciso1,
                            2:self.inciso2,
                            3:self.inciso3,
                            4:self.inciso4,
                            5:self.inciso5,
                            6:self.inciso6,
                         }
        self.__viajeros = viajeros

    def getSwitcher(self):
        return self.__switcher

    def option(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Fin programa')

    def inciso1(self):
        num_viajero = int(input('Ingrese un numero de viajero frecuente: '))        
        self.__viajeros.consultar_millas(num_viajero)


    def inciso2(self):
        num_viajero = int(input('Ingrese un numero de viajero frecuente: '))        
        millas_recorridas = int(input("Ingrese las millas recorridas: "))
        self.__viajeros.acumular_millas(num_viajero, millas_recorridas)

    def inciso3(self):
        num_viajero = int(input('Ingrese un numero de viajero frecuente: '))
        millas_a_canjear = int(input("Ingrese las millas a canjear: "))
        self.__viajeros.canjear_millas(num_viajero, millas_a_canjear)

    def inciso4(self):
        self.__viajeros.mostrar_viajeros_con_mayor_millas_acumuladas()

    def inciso5(self):
        num_viajero = int(input('Ingrese un numero de viajero frecuente: '))
        entero = int(input('Ingrese un numero entero: '))
        self.__viajeros.comparar_millas_acumuladas_con_un_entero_izq(num_viajero, entero)
    
    def inciso6(self):
        num_viajero = int(input('Ingrese un numero de viajero frecuente: '))
        entero = int(input('Ingrese un numero entero: '))
        self.__viajeros.comparar_millas_acumuladas_con_un_entero_der(num_viajero, entero)