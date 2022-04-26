import csv

from claseMenu import Menu

from claseLista import Lista

from clasePlanAhorro import PlanAhorro

def leer_datos() -> Lista:
    planes = Lista()
    archivo = open('planes.csv')
    reader = csv.reader(archivo, delimiter=';')
    for fila in reader:
        planes.agregarPlan(PlanAhorro(int(fila[0]),
                                         fila[1],
                                         fila[2],
                                         float(fila[3])))
        if PlanAhorro.getCantidadCuotas() != int(fila[4]):
            PlanAhorro.setCantidadCuotas(int(fila[4]))
        if PlanAhorro.getCantCuotasPagas() != int(fila[5]):
            PlanAhorro.setCantidadCuotasPagas(int(fila[5]))
        #print('Cantidad cuotas del plan: {}, Cantidad cutas pagas necesarias para...: {}'.format(PlanAhorro.getCantidadCuotas(),
        #                                                                                         PlanAhorro.getCantCuotasPagas()))
    archivo.close()
    return planes

def menu(planes):
    menu = Menu(planes)
    exit = False
    while not exit:
        print("---------------MENU---------------\n"
              "1.Actualizar el valor del vehículo de cada plan.\n"
              "2.Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.\n"
              "3.Mostrar el monto que se debe haber pagado para licitar el vehículo.\n"
              "4.Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar..\n"
              "0.Salir")
        opt = int(input('Ingrese una opcion: '))
        menu.option(opt)
        exit = opt==0

if __name__ == '__main__':
    planes = leer_datos()
    menu(planes)
