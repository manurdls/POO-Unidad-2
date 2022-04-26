import csv

from claseMenu import Menu

from claseRegistro import Registro

def crear_lista():
    dias = []
    for i in range(30):
        horas = []
        for j in range(24):
            horas.append(None)
        dias.append(horas)
        del horas
    return dias

def cargar_datos(datos):
    archivo = open('datos.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        datos[int(fila[0])-1][int(fila[1])] = Registro(int(fila[2]), int(fila[3]), int(fila[4]))
    archivo.close()

def menu(datos):
    menu = Menu(datos)
    exit = False
    while not exit:
        print("---------------MENU---------------\n"
              "1.Mostrar para cada variable el día y hora de menor y mayor valor.\n"
              "2.Indicar la temperatura promedio mensual por cada hora.\n"
              "3.Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.\n"
              "0.Salir.")
        opt = int(input('Ingrese una opcion: '))
        menu.option(opt)
        exit = opt==0

if __name__ == '__main__':
    datos = crear_lista()
    cargar_datos(datos)
    menu(datos)
    
