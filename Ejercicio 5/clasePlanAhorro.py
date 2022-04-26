

class PlanAhorro(object):
    
    cant_cuotas = 10
    cant_cuotas_pagas_npl = 2

    __codigo_plan = None
    __modelo_vehiculo = None
    __version_vehiculo = None
    __valor_vehiculo = None

    def __init__(self, codigo_plan, modelo, version, valor):
        self.__codigo_plan = codigo_plan
        self.__modelo_vehiculo = modelo
        self.__version_vehiculo = version
        self.__valor_vehiculo = valor

    def __str__(self):
        s = 'Código del plan: ' + str(self.__codigo_plan) + ", "
        s += 'Modelo del vehículo: ' + self.__modelo_vehiculo + ", "
        s += 'Versión del vehículo: ' + self.__version_vehiculo + ", "
        s += 'Valor del vehículo: ' + str(self.__valor_vehiculo) + "."
        return s

    @classmethod
    def getCantidadCuotas(cls):
        return cls.cant_cuotas

    @classmethod
    def getCantCuotasPagas(cls):
        return cls.cant_cuotas_pagas_npl

    @classmethod
    def setCantidadCuotas(cls, cuotas):
        if type(cuotas) == int:
            cls.cant_cuotas = cuotas

    @classmethod
    def setCantidadCuotasPagas(cls, cuotas):
        if type(cuotas) == int:
            cls.cant_cuotas_pagas_npl = cuotas

    def getCodigo(self):
        return self.__codigo_plan

    def getModeloVehiculo(self):
        return self.__modelo_vehiculo

    def getVersionVehiculo(self):
        return self.__version_vehiculo

    def getValorVehiculo(self):
        return self.__valor_vehiculo

    def setValorVehiculo(self, nuevo_valor):
        if type(nuevo_valor) == float:
            self.__valor_vehiculo = nuevo_valor

    def getImporteCuota(self):
        return (self.getValorVehiculo()/PlanAhorro.getCantidadCuotas()) + (self.getValorVehiculo()*0.10)

    def getMontoParaLicitar(self):
        print(PlanAhorro.getCantCuotasPagas(), self.getImporteCuota())
        return PlanAhorro.getCantCuotasPagas() * self.getImporteCuota()