class Ventana(object):

    __titulo = None
    __vertice_sup_izq = None
    __vertice_inf_der = None

    def __init__(self, titulo, x_sup_izq=-1, y_sup_izq=0, x_inf_der=500, y_inf_der=500):
        
        if self._validar_datos(x_sup_izq, y_sup_izq, x_inf_der, y_inf_der):

            self.__titulo = titulo

            self.__vertice_sup_izq = []
            self.__vertice_sup_izq.append(x_sup_izq)
            self.__vertice_sup_izq.append(y_sup_izq)

            self.__vertice_inf_der = []
            self.__vertice_inf_der.append(x_inf_der)
            self.__vertice_inf_der.append(y_inf_der)
            
        else:

            del self

        

    def __str__(self):
        pass

    def _validar_datos(self, xsi, ysi, xid, yid):
        retorno = False

        if type(xsi) == int and type(ysi) == int and type(xid) == int and type(yid) == int:
            if xsi >= 0 and xsi < xid and ysi >= 0 and ysi < yid:
                retorno = True
        
        return retorno

    def mostrar(self):
        print('Vertice superior izquierdo: ({},{})'.format(self.__vertice_sup_izq[0],
                                                           self.__vertice_sup_izq[1]))
        print('Vertice inferior derecho: ({},{})'.format(self.__vertice_inf_der[0],
                                                         self.__vertice_inf_der[1]))

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return str(self.__vertice_inf_der[1]-self.__vertice_sup_izq[1])

    def ancho(self):
        return str(self.__vertice_inf_der[0]-self.__vertice_sup_izq[0])