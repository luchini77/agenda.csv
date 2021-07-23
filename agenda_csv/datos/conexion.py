import csv
import pathlib
from prettytable import from_csv
from prettytable import PrettyTable


nombre_archivo = 'datos/agenda.csv'
campos = ['NOMBRE','MOVIL','EMAIL']

class Agenda:

    def __init__(self):
        
        pass


    def existe_archivo(self):
    
        if not pathlib.Path(nombre_archivo).exists():
            
            return False


    def grabar(self, contacto):

        datos = [contacto.nombre,contacto.movil,contacto.email]

        if not pathlib.Path(nombre_archivo).exists():
            with open(nombre_archivo, 'w', newline='') as archivo_csv:
                writer = csv.DictWriter(archivo_csv, fieldnames=campos)
                writer.writeheader()

        with open(nombre_archivo, 'a', newline='') as archivo_csv:
            escribir = csv.writer(archivo_csv, delimiter=',')

            escribir.writerow(datos)


    def listar_contactos(self):

        fp = open(nombre_archivo,'r')
        tabla = from_csv(fp)
        fp.close()
        print(tabla)


    def buscar_contacto(self, contacto):

        with open(nombre_archivo) as archivo_csv:
            buscar = csv.reader(archivo_csv, delimiter=',')
            data = list(buscar)


            for row in data:
                if row[0] == contacto:

                    tabla = PrettyTable()
                    tabla.field_names = ['NOMBRE','MOVIL','EMAIL']
                    tabla.add_row(row)

                    print(tabla)
                    break
                    
            else:
                print()
                print('Contacto no encontrado')
                print()


    def modificar_contacto(self, datos):

        with open(nombre_archivo, 'r', newline='') as archivo_csv:
            buscar = csv.DictReader(archivo_csv)
            data = list(buscar)

        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            header = ('NOMBRE','MOVIL','EMAIL')

            escribir = csv.DictWriter(archivo_csv, fieldnames=header, lineterminator='\n')
            escribir.writeheader()
            for row in data:
                if row['NOMBRE'] == datos[0]:
                    row['NOMBRE'] = datos[1]
                    row['MOVIL'] = datos[2]
                    row['EMAIL'] = datos[3]

                escribir.writerow(row)


    def elimiminar_contacto(self, contacto):

        with open(nombre_archivo, 'r', newline='') as archivo_csv:
            buscar = csv.DictReader(archivo_csv)
            data = list(buscar)

        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            header = ('NOMBRE','MOVIL','EMAIL')

            escribir = csv.DictWriter(archivo_csv, fieldnames=header, lineterminator='\n')
            escribir.writeheader()
            for row in data:
                if row['NOMBRE'] == contacto:
                    continue
                escribir.writerow(row)

