from claseVertice import Vertice

class Ventana(object):

    __titulo = None
    __x_sup_izq = None
    __y_sup_izq = None
    __x_inf_der = None
    __y_inf_der = None

    def __init__(self, titulo, x_sup_izq=100, y_sup_izq=100, x_inf_der=400, y_inf_der=400):
        
        if self._validar_datos(x_sup_izq, y_sup_izq, x_inf_der, y_inf_der):

            self.__titulo = titulo

            self.__x_sup_izq = x_sup_izq
            self.__y_sup_izq = y_sup_izq
            self.__x_inf_der = x_inf_der
            self.__y_inf_der = y_inf_der

        

    def __str__(self):
        pass

    def _validar_datos(self, xsi, ysi, xid, yid):

        if type(xsi) != int or type(ysi) != int or type(xid) != int or type(yid) != int:
            raise TypeError('El valor de las componentes de los vértices de una ventana deben ser de tipo int')

        if xsi < 0 or ysi < 0:
            raise Exception('Los valores de x e y del vértice superior izquierdo no pueden ser menores a 0')

        if xid > 500 or yid > 500:
            raise Exception('Los valores de x e y del vértice inferior derecho no pueden ser mayores a 500')

        if xsi >= xid:
            raise Exception('El valor de x del vértice superior izquierdo debe ser menor al valor de x del vértice inferior derecho')

        if ysi >= yid:
            raise Exception('El valor de y del vértice superior izquierdo debe ser menor al valor de y del vértice inferior derecho.')

        return True

    def mostrar(self):
        print('Vertice superior izquierdo: ({},{})'.format(self.__x_sup_izq,
                                                           self.__y_sup_izq))
        print('Vertice inferior derecho: ({},{})'.format(self.__x_inf_der,
                                                         self.__y_inf_der))

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return str(self.__y_inf_der-self.__y_sup_izq)

    def ancho(self):
        return str(self.__x_inf_der-self.__x_sup_izq)

    def moverDerecha(self, unidades=1):
        nuevo_x_sup_izq = self.__x_sup_izq + unidades
        nuevo_x_inf_der = self.__x_inf_der + unidades
        if nuevo_x_inf_der > 500:
            raise Exception('Ventana fuera de rango')
        else:
            self.__x_sup_izq = nuevo_x_sup_izq
            self.__x_inf_der = nuevo_x_inf_der

    def moverIzquierda(self, unidades=1):
        nuevo_x_sup_izq = self.__x_sup_izq - unidades
        nuevo_x_inf_der = self.__x_inf_der - unidades

        if nuevo_x_sup_izq < 0:
            raise Exception('Ventana fuera de rango')
        else:
            self.__x_inf_der = nuevo_x_inf_der

    def bajar(self, unidades=1):
        nuevo_y_sup_izq = self.__y_sup_izq + unidades
        nuevo_y_inf_der = self.__y_inf_der + unidades

        if nuevo_y_inf_der > 500:
            raise Exception('Ventana fuera de rango')
        else:
            self.__y_sup_izq = nuevo_y_sup_izq
            self.__y_inf_der = nuevo_y_inf_der

    def subir(self, unidades=1):
        nuevo_y_sup_izq = self.__y_sup_izq - unidades
        nuevo_y_inf_der = self.__y_inf_der - unidades

        if nuevo_y_sup_izq < 0:
            raise Exception('Ventana fuera de rango')
        else:
            self.__y_sup_izq = nuevo_y_sup_izq
            self.__y_inf_der = nuevo_y_inf_der
