class Menu(object):
    __switcher = None
    __datos = None

    def __init__(self, datos=None):
        self.__switcher = { 0:self.salir,
                            1:self.inciso1,
                            2:self.inciso2,
                            3:self.inciso3,
                         }
        self.__datos = datos

    def getSwitcher(self):
        return self.__switcher

    def option(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Fin programa')

    def inciso1(self):
        dias_menor_temperatura = []
        dias_mayor_temperatura = []
        dias_menor_humedad = []
        dias_mayor_humedad = []
        dias_menor_presion = []
        dias_mayor_presion = []

        temperatura_minima = 300
        temperatura_maxima = -300
        humedad_minima = 300
        humedad_maxima = -300
        presion_minima = 10000
        presion_maxima = 0

        for i in range(len(self.__datos)):
            for j in range(len(self.__datos[i])):
                temperatura = self.__datos[i][j].get_temperatura()
                humedad = self.__datos[i][j].get_humedad()
                presion = self.__datos[i][j].get_presion()

                if temperatura <= temperatura_minima:
                    if temperatura < temperatura_minima:
                        temperatura_minima = temperatura
                        dias_menor_temperatura = []
                    dias_menor_temperatura.append((i, j))
                if temperatura >= temperatura_maxima:
                    if temperatura > temperatura_maxima:
                        temperatura_maxima = temperatura
                        dias_mayor_temperatura = []
                    dias_mayor_temperatura.append((i, j))

                if humedad <= humedad_minima:
                    if humedad < humedad_minima:
                        humedad_minima = humedad
                        dias_menor_humedad = []
                    dias_menor_humedad.append((i, j))
                if humedad >= humedad_maxima:
                    if humedad > humedad_maxima:
                        humedad_maxima = humedad
                        dias_mayor_humedad = []
                    dias_mayor_humedad.append((i, j))

                if presion <= presion_minima:
                    if presion < presion_minima:
                        presion_minima = presion
                        dias_menor_presion = []
                    dias_menor_presion.append((i, j))
                if presion >= presion_maxima:
                    if presion > presion_maxima:
                        presion_maxima = presion
                        dias_mayor_presion = []
                    dias_mayor_presion.append((i, j))
        
        print('Menor temperatura registrada: {} \nDias y horas en que se registró: '.format(temperatura_minima))
        for dias in dias_menor_temperatura:
            print('Dia: {}, Hora: {}'.format(dias[0]+1, dias[1]))
        
        print('Mayor temperatura registrada: {} \nDias y horas en que se registró: '.format(temperatura_maxima))
        for dias in dias_mayor_temperatura:
            print('Dia: {}, Hora: {}'.format(dias[0]+1, dias[1]))

        print('Menor humedad registrada: {} \nDias y horas en que se registró: '.format(humedad_minima))
        for dias in dias_menor_humedad:
            print('Dia: {}, Hora: {}'.format(dias[0]+1, dias[1]))

        print('Mayor humedad registrada: {} \nDias y horas en que se registró: '.format(humedad_maxima))
        for dias in dias_mayor_humedad:
            print('Dia: {}, Hora: {}'.format(dias[0]+1, dias[1]))

        print('Menor presion registrada: {} \nDias y horas en que se registró: '.format(presion_minima))
        for dias in dias_menor_presion:
            print('Dia: {}, Hora: {}'.format(dias[0]+1, dias[1]))

        print('Mayor presion registrada: {} \nDias y horas en que se registró: '.format(presion_maxima))
        for dias in dias_mayor_presion:
            print('Dia: {}, Hora: {}'.format(dias[0]+1, dias[1]))


    def inciso2(self):
        promedios_temperatura = []
        for i in range(24): promedios_temperatura.append(0)

        for i in range(len(self.__datos)):
            for j in range(len(self.__datos[i])):
                promedios_temperatura[j] += self.__datos[i][j].get_temperatura()

        promedios_temperatura = list(map(lambda x: x / len(self.__datos), promedios_temperatura))

        for i in range(len(promedios_temperatura)):
            print('La temperatura promedio para la/s {} hs fue: {}°.'.format(i, promedios_temperatura[i]))

    def inciso3(self):
        dia = int(input('Ingrese un número de día:'))

        s = 'Hora      Temperatura      Humedad      Presión'
        print(s)

        for hora in range(len(self.__datos[dia-1])):
            print('{0:02d} {1:13d} {2:14d} {3:13d}'.format(hora,
                                                        self.__datos[dia-1][hora].get_temperatura(),
                                                        self.__datos[dia-1][hora].get_humedad(),
                                                        self.__datos[dia-1][hora].get_presion()))
    