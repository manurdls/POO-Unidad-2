from re import M
from clasePlanAhorro import PlanAhorro

class Lista(object):

    __planes = None

    def __init__(self):
        
        self.__planes = []

    def agregarPlan(self, plan):
        if isinstance(plan, PlanAhorro):
            self.__planes.append(plan)

    def mostrarPlanes(self):
        for plan in self.__planes:
            print(plan)

    def _buscar_plan_por_codigo(self, codigo):
        retorno = None
        band = False
        i = 0
        cant_planes = len(self.__planes)
        while not band and i < cant_planes:
            if self.__planes[i].getCodigo() == codigo:
                band = True
                retorno = i
            i += 1
        if band == False:
            print("No se encontró un Plan de Ahorro cuyo número código sea: {}".format(codigo))
        return retorno

    def actualizar_valor_vehiculo_de_cada_plan(self):
        print("A continuación, ingrese el nuevo valor de los vehículos: ")
        for plan in self.__planes:
            nuevo_valor = float(input('Codigo del plan: {}, Modelo vehículo: {}, Versión vehículo: {}, Nuevo valor: '.format(plan.getCodigo(),
                                                                                                                             plan.getModeloVehiculo(),
                                                                                                                             plan.getVersionVehiculo())))
            plan.setValorVehiculo(nuevo_valor)
    
    def mostrar_planes_cuya_cuta_no_supere_un_monto(self, monto):
        band = False
        for plan in self.__planes:
            if plan.getValorVehiculo() < monto:
                if not band:
                    print('Los planes cuyo valor de vehículo no superan los {} pesos son: '.format(monto))
                    band = True
                print('Codigo del plan: {}, Modelo vehículo: {}, Versión vehículo: {}'.format(plan.getCodigo(),
                                                                                              plan.getModeloVehiculo(),
                                                                                              plan.getVersionVehiculo()))
        if not band:
            print("Disculpe, en este momento no hay planes cuyo valor de vehículo sea inferior a {} pesos.".format(monto))

    def monto_a_pagar_necesario_para_licitar(self, codigo_plan):
        indice_plan = self._buscar_plan_por_codigo(codigo_plan)
        if indice_plan != None:
            print("Monto necesario para licitar: {:.3f} pesos.".format(self.__planes[indice_plan].getMontoParaLicitar()))