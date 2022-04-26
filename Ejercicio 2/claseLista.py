from claseViajeroFrecuente import ViajeroFrecuente

class Lista(object):

    __viajeros = None

    def __init__(self):
        
        self.__viajeros = []

    def agregarViajero(self, viajero):
        if isinstance(viajero, ViajeroFrecuente):
            self.__viajeros.append(viajero)

    def mostrarViajeros(self):
        for viajero in self.__viajeros:
            print(viajero)

    def _buscar_viajero_por_num_viajero(self, num_viajero):
        retorno = None
        band = False
        i = 0
        cant_viajeros = len(self.__viajeros)
        while not band and i < cant_viajeros:
            if self.__viajeros[i].getNumViajero() == num_viajero:
                band = True
                retorno = i
            i += 1
        if band == False:
            print("No se encontró un viajero frecuente cuyo número de viajero sea: {}".format(num_viajero))
        return retorno

    def consultar_millas(self, num_viajero):
        indice_viajero = self._buscar_viajero_por_num_viajero(num_viajero)
        if indice_viajero != None:
            print("Numero viajero frecuente: {}, Millas Acumuladas: {}".format(self.__viajeros[indice_viajero],
                                                                               self.__viajeros[indice_viajero].cantidadTotalMillas()))

    def acumular_millas(self, num_viajero, millas_recorridas):
        indice_viajero = self._buscar_viajero_por_num_viajero(num_viajero)
        if indice_viajero != None:
            print("Numero viajero frecuente: {}, Millas Acumuladas: {}".format(self.__viajeros[indice_viajero],
                                                                               self.__viajeros[indice_viajero].acumularMillas(millas_recorridas)))

    def canjear_millas(self, num_viajero, millas_a_canjear):
        indice_viajero = self._buscar_viajero_por_num_viajero(num_viajero)
        if indice_viajero != None:
            print("Numero viajero frecuente: {}, Millas Acumuladas: {}".format(self.__viajeros[indice_viajero],
                                                                               self.__viajeros[indice_viajero].canjearMillas(millas_a_canjear)))
