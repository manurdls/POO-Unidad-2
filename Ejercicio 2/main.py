import csv

from claseMenu import Menu

from claseLista import Lista

from claseViajeroFrecuente import ViajeroFrecuente

def leer_datos() -> Lista:
    viajeros = Lista()
    archivo = open('datos.csv')
    reader = csv.reader(archivo, delimiter=';')
    for fila in reader:
        viajeros.agregarViajero(ViajeroFrecuente(int(fila[0]),
                                         fila[1],
                                         fila[2],
                                         fila[3],
                                         int(fila[4])))
    archivo.close()
    return viajeros

def menu(viajeros, num_viajero):
    menu = Menu(viajeros, num_viajero)
    exit = False
    while not exit:
        print("---------------MENU---------------\n"
              "1.Consultar cantidad de millas.\n"
              "2.Acumular millas.\n"
              "3.Canjear millas.\n"
              "0.Salir")
        opt = int(input('Ingrese una opcion: '))
        menu.option(opt)
        exit = opt==0

if __name__ == '__main__':
    viajeros = leer_datos()
    num_viajero = int(input('Ingrese un numero de viajero frecuente: '))
    menu(viajeros, num_viajero)