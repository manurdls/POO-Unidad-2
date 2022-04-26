from claseLista import Lista

from clasePlanAhorro import PlanAhorro

class Menu(object):
    __switcher = None
    __planes = None

    def __init__(self, planes):
        self.__switcher = { 0:self.salir,
                            1:self.inciso1,
                            2:self.inciso2,
                            3:self.inciso3,
                            4:self.inciso4,
                         }
        self.__planes = planes

    def getSwitcher(self):
        return self.__switcher

    def option(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Fin programa')

    def inciso1(self):
        #self.__planes.mostrarPlanes()
        self.__planes.actualizar_valor_vehiculo_de_cada_plan()
        #self.__planes.mostrarPlanes()

    def inciso2(self):
        monto = float(input("Ingrese un monto: "))
        self.__planes.mostrar_planes_cuya_cuta_no_supere_un_monto(monto)

    def inciso3(self):
        codigo_plan = int(input("Ingrese el código del plan: "))
        self.__planes.monto_a_pagar_necesario_para_licitar(codigo_plan)

    def inciso4(self):
        print("No tiene sentido, porque las cuotas pagas necesarias para licitar son compartidas por todos los planes")
